# 📄 Resume AI Analyzer

## Project Overview  
**Resume AI Analyzer** is a smart web application that allows users to upload a resume in PDF format and check how well it matches a specific job role (e.g., Frontend Developer, Data Scientist, etc.).

It uses Natural Language Processing (NLP) to extract, analyze, and summarize key information from resumes, helping both recruiters and candidates make informed decisions.

---

## ❓ Problem Statement  
Recruiters often spend a lot of time manually screening resumes.  
Candidates are also unaware of how suitable their resume is for a specific role.

This project solves both problems by:
- Automatically analyzing the resume
- Matching extracted skills with job requirements
- Showing matched and missing skills
- Declaring suitability (Suitable / Not Suitable)
- Generating a short summary of the resume

---

## 🛠️ How It Works  

### 1. Frontend Interface  
- Built using **Streamlit**  
- Simple UI to upload PDF and enter job role

### 2. PDF Text Extraction  
- Done using **PyMuPDF (fitz)** or **pdfminer**

### 3. Resume Analysis  
- **spaCy** is used to extract keywords and skills  
- Skills are matched with pre-defined job role skill sets such as:
  - Frontend Developer
  - Backend Developer
  - Data Scientist
  - AI Engineer
  - Full Stack Developer

### 4. Suitability Check  
- Compares extracted skills to the job's required skills  
- Displays:
  - ✅ Matched Skills
  - ❌ Missing Skills
  - 🎯 Suitability Result

### 5. Summary Generation  
- Uses **Sumy** or **NLTK** to generate a 200–300 word summary

---

## 🧪 Technologies Used  
- **Python**  
- **Streamlit** – Web app framework  
- **spaCy** – NLP and skill extraction  
- **PyMuPDF** / **pdfminer** – PDF text extraction  
- **NLTK / Sumy** – Resume summarization

---

## 🔧 Why These Tools Were Used  
- **Python** – Easy integration of AI/NLP libraries  
- **Streamlit** – Fast UI development  
- **spaCy** – Accurate NLP model for skill extraction  
- **PyMuPDF** – High-speed PDF reading  
- **Sumy / NLTK** – Readymade summarization logic

---

## 🔮 Future Improvements  
- Integrate **OpenAI/GPT API** for smarter matching  
- Upload job descriptions as PDF  
- Generate **resume score (0–100)**  
- Export analysis as **PDF report**

---

## 👤 Author  
**Farhan Akthar**  
Open to opportunities in AI/ML, NLP, and Python development  
[GitHub Profile](https://github.com/farhan563)
