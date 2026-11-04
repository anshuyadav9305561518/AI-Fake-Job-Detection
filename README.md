# 🔍 AI-Based Fake Job Detection System

### Machine Learning Project | NLP | Python | Streamlit

An AI-powered web application that identifies potentially fraudulent job postings using Natural Language Processing (NLP) and Machine Learning.

## 🚀 Live Demo

Try the application here:

https://ai-fake-job-detection-k27uksxfabtnaf3rz8u6r6.streamlit.app/

## 📌 Project Overview

Online job fraud is a growing problem. This project uses Machine Learning to analyze job descriptions and predict whether a job posting is Genuine or potentially Fake.

Users can enter job details and receive a prediction with model-estimated scores.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- TF-IDF Vectorization
- Logistic Regression
- Random Forest
- Streamlit
- Matplotlib
- Seaborn

## ⚙️ Project Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Text Preprocessing
5. Natural Language Processing
6. TF-IDF Feature Extraction
7. Model Training
8. Model Evaluation
9. Model Deployment using Streamlit

## 🤖 Machine Learning Models

Two models were trained and evaluated:

| Model | Accuracy | Fake Job Recall |
|---|---:|---:|
| Logistic Regression | 96.90% | 90.80% |
| Random Forest | 98.18% | 65.30% |

### Final Model: Logistic Regression

Logistic Regression was selected because it achieved higher recall for fake job postings, helping identify more potentially fraudulent listings.

## 📊 Model Evaluation

Logistic Regression Confusion Matrix:

| | Predicted Genuine | Predicted Fake |
|---|---:|---:|
| Actual Genuine | 3308 | 95 |
| Actual Fake | 16 | 157 |

## 💻 Run Locally

Clone the repository:

```bash
git clone https://github.com/anshuyadav9305561518/AI-Fake-Job-Detection.git
