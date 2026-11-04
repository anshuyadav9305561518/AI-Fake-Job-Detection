# 🤖 AI-Based Fake Job Detection System

## 📌 Project Overview

This project is an AI-Based Fake Job Detection System developed using Python, Machine Learning, and Natural Language Processing (NLP).

The system analyzes job descriptions and predicts whether a job posting is Genuine or Fake.

## 🎯 Project Objectives

* Detect fraudulent job postings.
* Analyze job descriptions using NLP.
* Apply TF-IDF Vectorization.
* Train and compare Machine Learning models.
* Predict whether a job is genuine or fake.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* Matplotlib
* Seaborn
* Joblib
* TF-IDF Vectorization

## 📊 Dataset Information

* Total Records: 17,880
* Total Features: 18
* Genuine Jobs: 17,014
* Fake Jobs: 866

## 🤖 Machine Learning Models

1. Logistic Regression
2. Random Forest Classifier

## 📈 Model Performance

| Metric             | Logistic Regression | Random Forest |
| ------------------ | ------------------: | ------------: |
| Accuracy           |              96.90% |        98.18% |
| Fake Job Precision |               62.3% |         95.8% |
| Fake Job Recall    |               90.8% |         65.3% |
| Fake Job F1 Score  |               73.9% |         77.7% |

### Final Model Selection

Logistic Regression was selected as the final model because it achieved higher recall (90.8%) for detecting fake job postings.

## ⚙️ Project Features

* Data Cleaning and Preprocessing
* Duplicate Removal
* Stopwords Removal
* Text Processing using NLP
* TF-IDF Feature Extraction
* Machine Learning Model Training
* Model Comparison
* Fake Job Prediction
* Model Saving using Joblib

## 📁 Project Files

* `Fake_Job_Detection.py` – Main Python code
* `DataSet.csv` – Original dataset
* `NLP_Cleaned_Data.csv` – Cleaned text dataset
* `logistic_regression_model.pkl` – Trained Logistic Regression model
* `tfidf_vectorizer.pkl` – Saved TF-IDF vectorizer

## 🚀 Future Improvements

* Develop a Streamlit web application.
* Improve model performance.
* Add real-time job posting detection.
* Use advanced NLP techniques.

## 👨‍💻 Author

**Anshu Yadav**

Aspiring Data Analyst | Machine Learning Enthusiast

* GitHub: https://github.com/anshuyadav9305561518
* LinkedIn: https://linkedin.com/in/anshu-yadav-a57917289
* Portfolio: https://anshuyadav9305561518.github.io/Portfolio-/

---

⭐ Thank you for visiting my project!
