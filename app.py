import streamlit as st
import pdfplumber
from resume_parser import extract_skills
from resume_score import score_resume

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

if uploaded_file is not None:
    text = extract_text(uploaded_file)

    skills = extract_skills(text)
    score = score_resume(text)

    st.subheader("Extracted Skills")
    st.write(skills)

    st.subheader("Resume Score")
    st.write(score)

    if score < 8:
        st.warning("Improve your resume with more keywords and strong project descriptions.")
    else:
        st.success("Good resume!")
