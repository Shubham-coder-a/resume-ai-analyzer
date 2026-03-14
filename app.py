import streamlit as st
import pdfplumber

skills = [
"python","java","sql","machine learning",
"react","javascript","html","css"
]

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()
    return text

def find_skills(text):
    found = []
    for skill in skills:
        if skill in text.lower():
            found.append(skill)
    return found

if uploaded_file is not None:

    text = extract_text(uploaded_file)

    found_skills = find_skills(text)

    score = len(found_skills)

    st.subheader("Detected Skills")
    st.write(found_skills)

    st.subheader("Resume Score")
    st.write(f"{score}/10")

    if score < 5:
        st.warning("Your resume needs improvement")
    else:
        st.success("Good resume!")
