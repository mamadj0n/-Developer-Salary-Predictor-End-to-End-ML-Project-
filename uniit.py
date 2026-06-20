from re import split

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

country = [
    "Ukraine",
    "Netherlands",
    "Australia",
    "United States of America",
    "United Kingdom of Great Britain and Northern Ireland",
    "Sweden",
    "Germany",
    "Czech Republic",
    "Switzerland",
    "Austria",
    "Poland",
    "Spain",
    "France",
    "Romania",
    "Canada",
    "Belgium",
    "Brazil",
    "Italy",
    "India",
    "Portugal",
    "Denmark",
]

EdLevel = [
    "High School or Less",
    "Some College",
    "Bachelor or Equivalent",
    "Master or Higher",
    "Other",
]

languages = [
    "SQL",
    "Python",
    "HTML/CSS",
    "JavaScript",
    "Bash/Shell (all shells)",
    "TypeScript",
    "C#",
    "Java",
    "Rust",
    "C++",
    "Go",
    "PowerShell",
    "C",
    "PHP",
]

DevType = [
    "Developer, full-stack",
    "Developer, back-end",
    "Student",
    "Architect, software or solutions",
    "Developer, front-end",
    "Developer, desktop or enterprise applications",
    "Other (please specify):",
    "Developer, mobile",
    "Developer, embedded applications or devices",
    "Academic researcher",
    "Engineering manager",
    "DevOps engineer or professional",
    "Data engineer",
    "AI/ML engineer",
    "Data scientist",
    "Senior executive (C-suite, VP, etc.)",
    "System administrator",
    "Retired",
    "Developer, game or graphics",
    "Cloud infrastructure engineer",
    "Founder, technology or otherwise",
    "Cybersecurity or InfoSec professional",
    "Data or business analyst",
    "Developer, QA or test",
    "Project manager",
    "Applied scientist",
    "Support engineer or analyst",
    "Developer, AI apps or physical AI",
    "Product manager",
    "Database administrator or engineer",
    "UX, Research Ops or UI design professional",
    "Financial analyst or engineer",
]

RemoteWork = [
    "Remote",
    "Hybrid (some remote, leans heavy to in-person)",
    "In-person",
    "Hybrid (some in-person, leans heavy to flexibility)",
    "Your choice (very flexible, you can come in when you want or just as needed)",
]

OrgSize = [
    "20 to 99 employees",
    "100 to 499 employees",
    "Less than 20 employees",
    "10,000 or more employees",
    "1,000 to 4,999 employees",
    "500 to 999 employees",
    "Just me - I am a freelancer, sole proprietor, etc.",
    "5,000 to 9,999 employees",
    "I don’t know",
]

Age = [
    "25-34 years old",
    "35-44 years old",
    "18-24 years old",
    "45-54 years old",
    "55-64 years old",
    "65 years or older",
    "Prefer not to say",
]

OpSysProfessional_use = [
    "Windows",
    "MacOS",
    "Ubuntu",
    "Windows Subsystem for Linux (WSL)",
    "iOS",
    "Android",
]

Industry = [
    "Software Development",
    "Other:",
    "Fintech",
    "Healthcare",
    "Banking/Financial Services",
    "Internet, Telecomm or Information Services",
    "Manufacturing",
    "Government",
    "Retail and Consumer Services",
    "Transportation, or Supply Chain",
    "Higher Education",
    "Energy",
    "Media & Advertising Services",
    "Computer Systems Design and Services",
    "Insurance",
]


class LanguageHaveWorkedWith_Transformer(BaseEstimator, TransformerMixin):
    def __init__(self, col="LanguageHaveWorkedWith"):
        self.col = col

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_transformed = X.copy()
        num_languages = []

        for row in X_transformed[self.col]:
            if pd.isna(row) or row == "":
                num_languages.append(0)
            else:
                try:
                    count = len(split(";", str(row)))
                    num_languages.append(count)
                except:
                    num_languages.append(0)

        X_transformed[self.col] = num_languages
        return X_transformed

    def get_feature_names_out(self, input_features=None):
        return np.array([self.col])


class EncodeEdLevel_Transformer(BaseEstimator, TransformerMixin):
    """
    Transformer برای ساده‌سازی و کدگذاری سطح تحصیلات
    """

    def __init__(self, col="EdLevel"):

        self.col = col

        self.education_mapping = {
            "High School or Less": 0,
            "Some College": 1,
            "Bachelor or Equivalent": 2,
            "Master or Higher": 3,
            "Other": 1,
        }

    def fit(self, X, y=None):
        """
        مرحله fit - هیچ محاسبه خاصی نیاز نیست
        """
        return self

    def transform(self, X):
        # ایجاد کپی از داده‌ها برای جلوگیری از تغییر داده اصلی
        X_transformed = X.copy()

        # تعریف تابع ساده‌سازی در داخل transform
        def simplify_education(level):

            if pd.isna(level) or level == "":
                return np.nan

            level = str(level)  # تبدیل به رشته برای امنیت بیشتر

            # بررسی ترتیب اهمیت: از بالاترین به پایین‌ترین
            if (
                "Master" in level
                or "Professional" in level
                or "PhD" in level
                or "Doctorate" in level
            ):
                return "Master or Higher"
            elif "Bachelor" in level or "Other" in level:
                return "Bachelor or Equivalent"
            elif "Some college" in level or "Associate" in level:
                return "Some College"
            elif "Primary" in level or "Secondary" in level or "High School" in level:
                return "High School or Less"
            else:
                return "Other"

        # مرحله ۱: ساده‌سازی سطح تحصیلات
        X_transformed["EdLevel_Simplified"] = X_transformed[self.col].apply(
            simplify_education
        )

        # مرحله ۲: تبدیل به اعداد با استفاده از نگاشت
        X_transformed[self.col] = X_transformed["EdLevel_Simplified"].map(
            self.education_mapping
        )

        # مرحله ۳: حذف ستون موقت
        X_transformed.drop("EdLevel_Simplified", axis=1, inplace=True)

        return X_transformed

    def get_feature_names_out(self, input_features=None):
        """
        برای سازگاری با ColumnTransformer
        """
        if input_features is None:
            return np.array([self.col])
        return np.array([self.col])


class org_size_order_Transformer(BaseEstimator, TransformerMixin):
    def __init__(self, col="OrgSize"):
        self.col = col
        self.org_size_order = {
            "Just me - I am a freelancer, sole proprietor, etc.": 0,
            "Less than 20 employees": 1,
            "20 to 99 employees": 2,
            "100 to 499 employees": 3,
            "500 to 999 employees": 4,
            "1,000 to 4,999 employees": 5,
            "5,000 to 9,999 employees": 6,
            "10,000 or more employees": 7,
            "I don't know": 3,  # میانگین یا میانه
        }

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_transformer = X.copy()

        X_transformer[self.col] = X[self.col].map(self.org_size_order)

        X_transformer[self.col] = X_transformer[self.col].fillna(3)

        return X_transformer

    def get_feature_names_out(self, input_features=None):
        return np.array([self.col])


class age_order_Transformer(BaseEstimator, TransformerMixin):
    def __init__(self, col="Age"):
        self.col = col
        self.age_order = {
            "18-24 years old": 0,
            "25-34 years old": 1,
            "35-44 years old": 2,
            "45-54 years old": 3,
            "55-64 years old": 4,
            "65 years or older": 5,
            "Prefer not to say": 2,  # میانگین
        }

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_transformer = X.copy()

        X_transformer[self.col] = X[self.col].map(self.age_order)

        X_transformer[self.col] = X_transformer[self.col].fillna(3)

        return X_transformer

    def get_feature_names_out(self, input_features=None):
        return np.array([self.col])
