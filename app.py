from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

app = Flask(__name__)

# Load dataset from CSV file
def load_dataset():
    try:
        df = pd.read_csv('dataset.csv')
        # Combine source and plagiarized text into one list
        sentences = df['source_text'].tolist() + df['plagiarized_text'].tolist()
        return [sentence.strip() for sentence in sentences if isinstance(sentence, str)]
    except Exception as e:
        print(f"❌ Error loading dataset.csv: {e}")
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_plagiarism():
    input_text = request.form.get('input_text', '').strip()
    dataset = load_dataset()

    if not dataset:
        return render_template('index.html', result='⚠️ Dataset is empty or missing.')

    if not input_text:
        return render_template('index.html', result='⚠️ Please enter some text.')

    for sentence in dataset:
        texts = [input_text, sentence]
        vectorizer = TfidfVectorizer().fit_transform(texts)
        vectors = vectorizer.toarray()
        cosine_sim = cosine_similarity([vectors[0]], [vectors[1]])[0][0]

        print(f"Checking similarity: {cosine_sim:.2f}")

        if cosine_sim >= 0.4:
            return render_template('index.html', result='Plagiarism Detected! ❌')

    return render_template('index.html', result='No plagiarism found. ✅')

if __name__ == '__main__':
    app.run(debug=True)
