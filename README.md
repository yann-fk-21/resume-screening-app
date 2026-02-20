# Resume Screening Application

An intelligent web application powered by machine learning that automatically classifies resumes into different professional categories. The application uses pre-trained models to analyze resume content and identify the most appropriate professional category.

## Features

* **Automatic classification**: Analyzes and classifies resumes into 24 different professional categories
* **User-friendly interface**: Simple and intuitive web interface built with Streamlit
* **PDF support**: Automatic text extraction and analysis from PDF files
* **Text processing**: Automatic text cleaning and preprocessing for improved accuracy
* **Real-time prediction**: Instant results after uploading a resume

## Supported Categories

The application can classify resumes into the following categories:

* Data Science
* HR (Human Resources)
* Advocate
* Arts
* Web Designing
* Mechanical Engineer
* Sales
* Health and Fitness
* Civil Engineer
* Java Developer
* Business Analyst
* SAP Developer
* Automation Testing
* Electrical Engineering
* Operations Manager
* Python Developer
* DevOps Engineer
* Network Security Engineer
* PMO (Project Management Office)
* Database
* Hadoop
* ETL Developer
* DotNet Developer
* Blockchain
* Testing

## Technologies Used

* **Python**: Main programming language
* **Streamlit**: Web application framework
* **scikit-learn**: Machine learning library
* **NLTK**: Natural language processing
* **PyPDF2**: Text extraction from PDF files
* **joblib**: Model saving and loading
* **pandas**: Data manipulation
* **numpy**: Numerical computations

## Installation

### Prerequisites

* Python 3.7 or higher
* pip (Python package manager)

### Installation Steps

1. **Clone the repository** (or download the project)

   ```bash
   git clone https://github.com/yann-fk-21/resume-screening-app.git
   cd resume-screening-app
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**

   On Windows:

   ```bash
   venv\Scripts\activate
   ```

   On Linux/Mac:

   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Download NLTK data** (automatic on first launch)

   * Required data (stopwords, punkt) will be downloaded automatically when the application runs for the first time.

## Usage

1. **Run the application**

   ```bash
   streamlit run app.py
   ```

2. **Access the interface**

   * The application will automatically open in your browser.
   * The default URL is: `http://localhost:8501`

3. **Use the application**

   * Click on "Upload your resume here"
   * Select a PDF file containing your resume
   * Wait a few seconds for processing
   * The detected professional category will be displayed automatically

## Project Structure

```
resume-screening-app/
│
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── LICENSE                     # Project license
│
├── models/                     # Pre-trained machine learning models
│   ├── clf_model.pkl           # Classification model
│   └── tfidf_model.pkl         # TF-IDF vectorization model
│
├── dataset/                    # Training dataset
│   └── UpdatedResumeDataSet.csv
│
├── notebook/                   # Jupyter notebook for analysis and training
│   └── modeling.ipynb
│
└── utils/                      # Utilities
    └── utils.py                # Text cleaning functions
```

## Technical Workflow

1. **Text extraction**: Text is extracted from the uploaded PDF file
2. **Cleaning**: The text is cleaned (removal of URLs, special characters, etc.)
3. **Vectorization**: The cleaned text is transformed into a numerical vector using TF-IDF
4. **Classification**: The classification model predicts the professional category
5. **Display**: The result is shown to the user

## Models

The pre-trained models (`clf_model.pkl` and `tfidf_model.pkl`) are included in the `models/` folder. These models were trained on the `UpdatedResumeDataSet.csv` dataset and use:

* **TF-IDF Vectorizer**: To transform text into numerical features
* **Classifier**: Supervised classification model (see details in the `modeling.ipynb` notebook)

## Model Training

If you would like to retrain the models:

1. Open the `notebook/modeling.ipynb` notebook
2. Run all cells
3. The new models will be saved in the `models/` folder

## License

See the `LICENSE` file for more details.
