from analyzer import detect_skills
import streamlit as st
from resume_parser import extract_text_from_pdf

st.set_page_config(page_title="AI Resume Analyzer")

st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    st.success("Resume Uploaded Successfully")

    text = extract_text_from_pdf(uploaded_file)
skills = detect_skills(text)

st.subheader("Detected Skills")

for skill in skills:
    st.success(skill)
    st.subheader("Resume Content")

    st.text_area(
        "Extracted Text",
        text,
        height=400
    )