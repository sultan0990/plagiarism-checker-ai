# 🔍 Plagiarism Checker AI

A **machine learning-based plagiarism detection system** built using Flask and TF-IDF, trained on the MIT plagiarism detection dataset. This project provides a user-friendly web interface and supports AI-based plagiarism prediction using cosine similarity.

![Plagiarism Checker Screenshot](screenshot.png) <!-- Optional: Upload a screenshot to GitHub and update filename -->

---

## 🚀 Features

- ✅ Web-based plagiarism checker with clean UI
- ✅ Uses **TF-IDF + Cosine Similarity** to check similarity
- ✅ Trained using the **MIT Plagiarism Detection Dataset**
- ✅ Highlights plagiarism if similarity score exceeds threshold
- ✅ Option to run Jupyter Notebook for backend training/analysis

---

## 📂 Dataset Used

- Dataset: [MIT Plagiarism Detection Dataset (Kaggle)](https://www.kaggle.com/datasets)
- Format: CSV with source texts and paraphrased variants
- Preprocessing: Lowercasing, stopword removal, vectorization

---

## ⚙️ Tech Stack

| Technology        | Role                          |
|-------------------|-------------------------------|
| Python            | Core Language                 |
| Flask             | Web App Backend               |
| Sklearn           | TF-IDF, Cosine Similarity     |
| HTML + CSS        | Frontend Design               |
| Jupyter Notebook  | Training + Accuracy Evaluation|

---

## 📊 ML Pipeline

- Load Dataset
- Preprocess Text
- TF-IDF Vectorization
- Cosine Similarity Calculation
- Flag similarity > 0.4 as plagiarized

---

## 🧪 Accuracy & Model

- Preprocessing: Done using Scikit-learn
- Model: TF-IDF + Cosine Similarity
- Accuracy:
    - Training Accuracy: `~98%`
    - Testing Accuracy: `~95%`

---

## 💻 Run Locally

### 1. Clone Repository

```bash
git clone https://github.com/sultan0990/plagiarism-checker-ai.git
cd plagiarism-checker-ai
