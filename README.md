# 💰-Developer-Salary-Predictor-End-to-End-ML-Project-
An end-to-end Machine Learning project that estimates annual developer salaries based on the 2026 Stack Overflow Developer Survey data. This repository contains both the core data science research (model training, feature engineering) and a production-ready interactive web application.

🌟 Why this project? (For Recruiters)
Unlike simple tutorials, this project showcases a complete software engineering and data science lifecycle:

Data R&D: Full preprocessing, feature engineering, and hyperparameter tuning in Jupyter Notebook.

Production Deployment: A beautiful, highly customized, dark-themed UI built with Streamlit for corporate use.

📦 Project Structure
The repository is organized into two main sections to maintain clean-code principles:

research/: The data science sandbox.

training_model.ipynb: Contains Exploratory Data Analysis (EDA), handling missing values, encoding programming languages, and training the CatBoost/Scikit-Learn model.

results.csv: Evaluation metrics and prediction results from the test dataset.

app/: The production web application.

app.py: The frontend application with custom CSS styling.

uniit.py: Helper file containing clean mappings for countries, developer roles, and technologies.

model_SALARY_v1.4.joblib: The serialized, high-performance trained model ready for inference.

🛠️ Tech Stack & Libraries
Language: Python

Data Science: Pandas, NumPy, Joblib

Machine Learning: CatBoost / Scikit-Learn

Frontend/Deployment: Streamlit (HTML/CSS Customization)

🚀 How to Run Locally
1. Clone the repository
Bash
```
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```
2. Install dependencies
Bash
```
pip install -r requirements.txt
```
4. Launch the Web App
Bash
```streamlit run app/app.py```
📊 Model Insights
Inside the research/ directory, you can explore the feature importance graph. Factors like Country, Years of Experience, and specific Developer Roles were found to have the highest impact on the salary prediction logic.
