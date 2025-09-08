import joblib
import nltk
import streamlit as st
import PyPDF2

from utils.utils import clean_text

nltk.download('stopwords')
nltk.download('punkt')

clf_model = joblib.load("./models/clf_model.pkl")
tfidf = joblib.load("./models/tfidf_model.pkl")

class_map = {6: 'Data Science', 12: 'HR', 0: 'Advocate', 1: 'Arts', 24: 'Web Designing', 16: 'Mechanical Engineer', 22: 'Sales', 14: 'Health and fitness', 5: 'Civil Engineer', 15: 'Java Developer', 4: 'Business Analyst', 21: 'SAP Developer', 2: 'Automation Testing', 11: 'Electrical Engineering', 18: 'Operations Manager', 20: 'Python Developer', 8: 'DevOps Engineer', 17: 'Network Security Engineer', 19: 'PMO', 7: 'Database', 13: 'Hadoop', 10: 'ETL Developer', 9: 'DotNet Developer', 3: 'Blockchain', 23: 'Testing'}

def main():
    st.title("Resume Classifier")
    upload_file = st.file_uploader("Upload your resume here", type=["pdf"])
    resume_text = ""

    if upload_file is not None:
        try:
            if upload_file.type == "application/pdf":
                pdf_reader = PyPDF2.PdfReader(upload_file)
                resume_text = ""
                for page in pdf_reader.pages:
                    resume_text += page.extract_text()
            elif upload_file.type == "text/plain":
                resume_text = upload_file.getvalue().decode("utf-8")
            else:
                st.error("Please upload a valid resume file!")
                return
        except UnicodeError:
            st.error("Please upload a valid resume file!")
            return

        cleaned_resume = clean_text(resume_text)
        resume_vector = tfidf.transform([cleaned_resume])
        prediction = clf_model.predict(resume_vector)[0]
        class_name = class_map[prediction]
        st.success(f"Your resume is classified as **{class_name} resume!**")

if __name__ == "__main__":
    main()
