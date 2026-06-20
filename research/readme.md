# 🔬 Research & Model Development

This directory contains the core Data Science and Machine Learning experiments for the Salary Prediction project. It documents the journey from raw developer survey data to the final serialized model.

## 📋 Contents

* **`training_model.ipynb`**: The primary Jupyter Notebook covering:
  * **Exploratory Data Analysis (EDA):** Visualizing salary distributions, handling outliers, and analyzing feature correlations.
  * **Data Cleaning:** Handling missing variables and structuring categorical text.
  * **Feature Engineering:** Processing complex columns like `LanguageHaveWorkedWith` (multi-label engineering).
  * **Model Selection:** Comparing algorithms and fine-tuning the final model for optimum performance.
* **`results.csv`**: Evaluation outputs, test predictions, and performance logs from the model validation phase.
for dataset go to --> https://www.kaggle.com/datasets/aliaslam25/stack-overflow-developer-survey-2025?select=survey_results_public.csv
## 📊 Methodology & Insights

1. **Target Variable:** Annual compensation (converted and cleaned to represent realistic salary boundaries).
2. **Key Predictors:** Analysis showed that **Country**, **Years of Coding (`YearsCode`)**, and **Developer Role (`DevType`)** carry the highest feature importance in predicting baseline salaries.
3. **Model Framework:** The training pipeline utilizes robust handling for categorical data, optimized to avoid overfitting while preserving high variance across different tech industries.

## 🛠️ How to Replicate the Training

If you wish to re-run the experiments or retrain the model:
1. Ensure you have activated your environment and installed dependencies from the root `requirements.txt`.
2. Open the notebook via Jupyter Lab or VS Code:
```bash
   jupyter notebook research/training_model.ipynb
