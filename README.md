# 🔍 Plagiarism Checker AI - Machine Learning Project

A **machine learning-based plagiarism detection system** built with **Python**, **Flask**, and **TF-IDF with Cosine Similarity**. Trained using the **MIT Plagiarism Detection Dataset**, this project includes both backend model training and a user-friendly frontend for plagiarism checking.

![Plagiarism Checker Screenshot](screenshot.png) <!-- Optional: Add your UI screenshot -->

---

## 📌 Table of Contents

- [📚 Introduction](#-introduction)
- [📂 Dataset Used](#-dataset-used)
- [🧹 Preprocessing](#-preprocessing)
- [🧠 Machine Learning Model](#-machine-learning-model)
- [🌐 Web Interface (Flask)](#-web-interface-flask)
- [📊 Accuracy & Performance](#-accuracy--performance)
- [🚀 Features](#-features)
- [💻 Run Locally](#-run-locally)
- [🧪 Working Demo](#-working-demo)

---

## 📚 Introduction

Plagiarism detection is essential in education and research to ensure originality and integrity. This project leverages natural language processing (NLP) and machine learning to automatically detect plagiarized text from original content. Users can input texts and receive a similarity score indicating the degree of plagiarism.

---

## 📂 Dataset Used

- **Dataset**: [MIT Plagiarism Detection Dataset (Kaggle)](https://www.kaggle.com/datasets)
- **Content**: Pairs of original and plagiarized texts
- **Format**: CSV with source and variant text columns

---

## 🧹 Preprocessing

Before feeding data to the ML model, the following preprocessing is performed:

- ✅ Tokenization
- ✅ Lowercasing
- ✅ Punctuation removal
- ✅ Stopword removal
- ✅ TF-IDF vectorization

---

## 🧠 Machine Learning Model

- **Vectorizer**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Similarity Metric**: Cosine Similarity
- **Threshold**: Similarity score > 0.4 is flagged as plagiarized

---

## 🌐 Web Interface (Flask)

The Flask web app provides an intuitive UI:

- 📥 Users can input two text blocks
- 📈 Get a real-time similarity score
- 💡 Simple, responsive, and clean UI using HTML & CSS

---

## 📊 Accuracy & Performance

| Metric              | Result     |
|---------------------|------------|
| Training Accuracy   | ~98%       |
| Testing Accuracy    | ~95%       |

- Model trained and evaluated using Jupyter Notebook (Colab compatible)

---

## 🚀 Features

- ✅ AI-based Plagiarism Detection
- ✅ Clean & Responsive Web Interface
- ✅ Dataset Preprocessing Pipeline
- ✅ Model Training in Jupyter Notebook
- ✅ Cosine Similarity Based Scoring
- ✅ Ready for Demo & Evaluation

---

## 💻 Run Locally

### 🔧 Prerequisites

- Python 3.x
- pip (Python package manager)

### 📦 Installation Steps

```bash
git clone https://github.com/sultan0990/plagiarism-checker-ai.git
cd plagiarism-checker-ai
pip install -r requirements.txt
python app.py
