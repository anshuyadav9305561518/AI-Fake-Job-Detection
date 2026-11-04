import streamlit as st
import joblib
import re
import nltk
from nltk.corpus import stopwords

# Download stopwords
nltk.download('stopwords', quiet=True)

# Load model and vectorizer
model = joblib.load("logistic_regression_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

stop_words = set(stopwords.words('english')) - {'no', 'not', 'nor'}


# Text cleaning
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'<.*?>', ' ', text)
    text = re.sub(r'http\S+|www\S+', ' ', text)
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()

    words = text.split()
    words = [word for word in words if word not in stop_words]

    return ' '.join(words)


# Page configuration
st.set_page_config(
    page_title="AI Fake Job Detector",
    page_icon="🔍",
    layout="centered"
)

# Professional CSS
st.markdown("""
<style>
.stApp {
    background-color: #0e1117;
    color: white;
}

.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: #00d4ff;
    padding: 15px;
}

.subtitle {
    text-align: center;
    color: #b0bec5;
    font-size: 16px;
    margin-bottom: 30px;
}

div.stButton > button {
    background: linear-gradient(90deg, #0072ff, #00c6ff);
    color: white;
    border-radius: 10px;
    height: 50px;
    font-size: 17px;
    font-weight: bold;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)


# App heading
st.markdown(
    '<div class="main-title">🔍 AI Fake Job Detector</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Smart Machine Learning System for Detecting Fraudulent Job Postings</div>',
    unsafe_allow_html=True
)

st.divider()


# User inputs
title = st.text_input("Job Title")
company = st.text_area("Company Profile")
description = st.text_area("Job Description")
requirements = st.text_area("Job Requirements")
benefits = st.text_area("Job Benefits")


# Prediction button
if st.button("Check Job Authenticity", use_container_width=True):

    if not title.strip() and not description.strip():
        st.warning("Please enter a Job Title or Job Description.")

    else:

        # Combine job text
        job_text = " ".join([
            title,
            company,
            description,
            requirements,
            benefits
        ])

        # Clean text
        cleaned_text = clean_text(job_text)

        # Convert text into TF-IDF
        vector = tfidf.transform([cleaned_text])

        # Predict
        prediction = model.predict(vector)[0]

        # Calculate probabilities
        probabilities = model.predict_proba(vector)[0]

        class_probabilities = dict(
            zip(model.classes_, probabilities)
        )

        fake_probability = class_probabilities[1] * 100
        genuine_probability = class_probabilities[0] * 100

        st.divider()

        st.subheader("🔍 Job Detection Results")

        if prediction == 1:
            st.error("⚠️ FAKE JOB ALERT!")
            st.write("This job posting may be fraudulent.")

        else:
            st.success("✅ GENUINE JOB")
            st.write("The model predicts this job posting is genuine.")

        # Probability scores
        col1, col2 = st.columns(2)

        with col1:
            st.metric("Fake Job Score", f"{fake_probability:.2f}%")
            st.progress(float(fake_probability / 100))

        with col2:
            st.metric("Genuine Job Score", f"{genuine_probability:.2f}%")
            st.progress(float(genuine_probability / 100))

        st.caption(
            "These are model-estimated scores, not guaranteed probabilities. "
            "Always verify the employer independently."
        )