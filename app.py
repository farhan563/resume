import streamlit as st
import tempfile
from resume_parser import extract_text_from_pdf
from analyzer import analyze_resume
from suggestions import get_suggestions
from summarizer import generate_summary

# Define job keywords
job_keywords = {
    "frontend developer": ["html", "css", "javascript", "react", "frontend", "ui", "bootstrap"],
    "backend developer": ["python", "django", "nodejs", "api", "sql", "backend", "flask"],
    "data scientist": ["python", "machine learning", "statistics", "pandas", "numpy", "data", "model"],
    "ai engineer": ["python", "deep learning", "tensorflow", "pytorch", "nlp", "ai", "ml"],
    "full stack developer": ["html", "css", "javascript", "react", "nodejs", "api", "sql", "mongodb", "frontend", "backend"],
}

st.title("📄 Resume AI Analyzer")

uploaded_file = st.file_uploader("Upload your resume (PDF only)", type="pdf")
job_role = st.text_input("Enter job role (e.g., 'frontend developer')")

if uploaded_file and job_role:
    # Save uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        file_path = tmp_file.name

    # Extract text
    text = extract_text_from_pdf(file_path)

    # Generate summary
    summary = generate_summary(text, sentence_count=7)
    st.subheader("📝 Resume Summary (200–300 words):")
    st.write(summary)

    # Extract skills
    skills = analyze_resume(text)
    st.subheader("✅ Detected Resume Skills:")
    st.write(", ".join(skills))

    # Job role match
    role = job_role.lower().strip()
    if role in job_keywords:
        required = job_keywords[role]
        matched = set(skills) & set(required)
        missing = set(required) - set(skills)

        st.subheader("📊 Match Results")
        st.write(f"Matched Skills: {', '.join(matched)}")
        st.write(f"Missing Skills: {', '.join(missing)}")

        if len(matched) >= len(required) // 2:
            st.success("✅ This resume is **suitable** for the role.")
        else:
            st.error("❌ This resume is **not suitable** for the role.")
    else:
        st.warning(f"No predefined skills for the role: {job_role}")
