from dotenv import load_dotenv
import streamlit as st
import os
import PyPDF2
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Gemini Pro model
model = genai.GenerativeModel('gemini-1.5-pro')

# Core Functions
def get_gemini_response(input_text):
    try:
        response = model.generate_content(input_text)
        return response.text
    except Exception as e:
        st.error(f"Error with Gemini API: {str(e)}")
        return None

def input_pdf_text(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Prompt
input_prompt = """
As an experienced ATS (Applicant Tracking System), proficient in the technical domain encompassing Software Engineering, Data Science, Data Analysis, Big Data Engineering, Web Developer, Mobile App Developer, DevOps Engineer, Machine Learning Engineer, Cybersecurity Analyst, Cloud Solutions Architect, Database Administrator, Network Engineer, AI Engineer, Systems Analyst, Full Stack Developer, UI/UX Designer, IT Project Manager, and additional specialized areas, your objective is to meticulously assess resumes against provided job descriptions. In a fiercely competitive job market, your expertise is crucial in offering top-notch guidance for resume enhancement. Assign precise matching percentages based on the JD (Job Description) and meticulously identify any missing keywords with utmost accuracy.

resume: {text}
description: {jd}

I want the response in the following structure:
The first line indicates the percentage match with the job description (JD).
The second line presents a list of missing keywords.
The third section provides a profile summary.

Mention the title for all the three sections.
While generating the response put some space to separate all the three sections.
"""

# Streamlit Page Configuration
st.set_page_config(page_title="CareerCraft - Resume ATS Tracker", layout="wide")

# Define tabs
tabs = st.tabs(["Home", "Analyze Resume", "FAQ"])

with tabs[0]:
    col1, col2 = st.columns([2,1])
    with col1:
        st.title("CareerCraft")
        st.header("ATS-Optimized Resume Analyzer")
        st.markdown("""
            **Welcome to CareerCraft**, your ultimate tool for crafting ATS-optimized resumes. 
            Analyze your resume against job descriptions, identify gaps, and enhance your career prospects!
        """)
    with col2:
        st.image("images/icon1.png", width=150)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns([1,2])
    with col1:
        st.image("images/icon2.png", width=150)
    with col2:
        st.subheader("Wide Range of Offerings")
        offerings = [
            "ATS-Optimized Resume Analysis",
            "Resume Optimization",
            "Skill Enhancement",
            "Career Progression Guidance",
            "Tailored Profile Summaries",
            "Streamlined Application Process",
            "Personalized Recommendations",
            "Efficient Career Navigation"
        ]
        for offering in offerings:
            st.write(f"✅ {offering}")

with tabs[1]:
    col1, col2 = st.columns([2,1])
    with col1:
        st.subheader("Embark on Your Career Adventure!")
        st.markdown("""
            **Instructions:** 
            - Paste the job description in the text area below.
            - Upload your resume in PDF format.
            - Click "Submit" to get the analysis.
            - For testing, use any PDF file and a sample job description like 'Software Engineer with Python and Java experience.'
        """)
        job_description = st.text_area("Paste the Job Description", height=150, placeholder="Enter the job description here...")
        uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type="pdf", help="Upload a PDF file of your resume")
        if st.button("Submit", type="primary"):
            if uploaded_file is not None and job_description:
                with st.spinner("Analyzing your resume..."):
                    resume_text = input_pdf_text(uploaded_file)
                    full_prompt = input_prompt.format(text=resume_text, jd=job_description)
                    response = get_gemini_response(full_prompt)
                    if response:
                        st.success("Analysis Complete!")
                        st.subheader("Analysis Result")
                        st.write(response)
            else:
                st.error("Please provide both a job description and a resume.")
    with col2:
        st.image("images/icon3.png", width=150)

with tabs[2]:
    col1, col2 = st.columns([1,2])
    with col1:
        st.image("images/icon4.png", width=150)
    with col2:
        st.subheader("Frequently Asked Questions")
        faqs = [
            ("How does CareerCraft analyze resumes and job descriptions?", 
             "CareerCraft uses advanced algorithms to analyze resumes and job descriptions, identifying key keywords and assessing compatibility between the two."),
            ("Can CareerCraft suggest improvements for my resume?", 
             "Yes, CareerCraft provides personalized recommendations to optimize your resume for specific job openings, including suggestions for missing keywords and alignment with desired job roles."),
            ("Is CareerCraft suitable for both entry-level and experienced professionals?", 
             "Absolutely! CareerCraft caters to job seekers at all career stages, offering tailored insights and guidance to enhance their resumes and advance their careers.")
        ]
        for question, answer in faqs:
            with st.expander(question):
                st.write(answer)