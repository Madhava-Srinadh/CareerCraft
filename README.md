Resume ATS Tracker
Overview
The Resume ATS Tracker is a Streamlit-based application designed to help job seekers optimize their resumes by analyzing them against job descriptions using Google's Gemini Pro model. This tool provides a percentage match, identifies missing keywords, and generates a profile summary to enhance your job application process.
Features

ATS-Optimized Analysis: Assesses resume compatibility with job descriptions.
Keyword Identification: Highlights missing keywords critical for job fit.
Profile Summary: Generates a concise summary based on your resume content.

Requirements

Python 3.7+
Required libraries (install via pip):
streamlit
python-dotenv
PyPDF2
google-generativeai



Installation
1. Clone the Repository
git clone https://github.com/your-username/resume-ats-tracker.git
cd resume-ats-tracker

2. Set Up a Virtual Environment (Optional but Recommended)
python -m venv venv
# On Windows: venv\Scripts\activate
# On Mac/Linux: source venv/bin/activate

3. Install Dependencies
Install the required libraries using the provided requirements.txt file:
pip install -r requirements.txt

4. Configure Google API Key

Obtain an API key from Google AI Studio.

Create a .env file in the project root and add your API key:
GOOGLE_API_KEY=your_api_key_here


Ensure .env is added to .gitignore to keep it secure.


Usage

Run the application:
streamlit run app.py


Open your browser and navigate to http://localhost:8501.

Enter a job description in the text area.

Upload your resume in PDF format.

Click "Analyze" to view the results, including match percentage, missing keywords, and a profile summary.


Project Structure
Resume ATS Tracker/
├── .env              # Stores the Google API key
├── app.py            # Main application file with Streamlit UI and model logic
├── requirements.txt  # Lists required libraries
├── .gitignore        # Excludes sensitive files from version control

