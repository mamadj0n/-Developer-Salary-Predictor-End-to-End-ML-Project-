import joblib
import pandas as pd
import streamlit as st
from unit import *

st.set_page_config(page_title="Salary Predictor", page_icon="💰", layout="wide")

st.markdown(
    """
<style>

/* Main Background */
.stApp{
    background: #0f172a;
    color: white;
}

/* Title */
.main-title{
    font-size: 3rem;
    font-weight: 700;
    text-align:center;
    margin-bottom:10px;
}

.subtitle{
    text-align:center;
    color:#94a3b8;
    margin-bottom:30px;
}

/* Cards */
[data-testid="stVerticalBlock"] > div{
    border-radius:18px;
}

/* Selectboxes */
.stSelectbox > div > div{
    background-color:#1e293b;
    border:1px solid #334155;
    border-radius:12px;
}

/* Multiselect */
.stMultiSelect > div > div{
    background-color:#1e293b;
    border:1px solid #334155;
    border-radius:12px;
}

/* Slider */
.stSlider{
    padding-top:15px;
}

/* Button */
.stButton button{
    width:100%;
    background:linear-gradient(
        90deg,
        #06b6d4,
        #3b82f6
    );
    color:white;
    font-size:18px;
    font-weight:600;
    border:none;
    border-radius:12px;
    padding:12px;
    transition:0.3s;
}

.stButton button:hover{
    transform:translateY(-2px);
    box-shadow:0 0 25px rgba(59,130,246,.4);
}

/* Prediction Card */
.prediction-card{
    background:#111827;
    border:1px solid #334155;
    border-radius:20px;
    padding:30px;
    text-align:center;
    margin-top:20px;
}

.prediction-value{
    font-size:2.5rem;
    font-weight:700;
    color:#22c55e;
}

.prediction-label{
    color:#94a3b8;
    font-size:1rem;
}

hr{
    border-color:#334155;
}

</style>
""",
    unsafe_allow_html=True,
)


# ۱. لود کردن مدل
model = joblib.load("app/model_SALARY_v1.4.joblib")

# ۲. Header
st.markdown(
    '<div class="main-title">Salary Prediction 2026</div>', unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Estimate your annual salary using developer profile data</div>',
    unsafe_allow_html=True,
)

# ۳. Input Section
col1, col2 = st.columns(2)

with col1:
    Country = st.selectbox("Country", country)

with col2:
    EdLevel = st.selectbox("Education Level", EdLevel)

col3, col4 = st.columns(2)

with col3:
    DevType = st.selectbox("Developer Role", DevType)

with col4:
    RemoteWork = st.selectbox("Work Mode", RemoteWork)

col5, col6 = st.columns(2)

with col5:
    OrgSize = st.selectbox("Company Size", OrgSize)

with col6:
    Age = st.selectbox("Age Range", Age)

col7, col8 = st.columns(2)

with col7:
    OpSysProfessionalUse = st.selectbox("Operating System", OpSysProfessional_use)

with col8:
    Industry = st.selectbox("Industry", Industry)

# Languages
selected_languages = st.multiselect("Programming Languages", languages)

LanguageHaveWorkedWith = ";".join(selected_languages)

# Sliders
JobSatPoints_1 = st.slider("Job Satisfaction", min_value=1, max_value=10, value=5)

YearsCode = st.slider("Years of Coding", min_value=1, max_value=45, value=10)

WorkExp = st.slider("Professional Experience", min_value=1, max_value=39, value=8)

st.markdown("---")

st.markdown("### Ready to estimate your salary?")

# ۴. ساخت دیتافریم ورودی
Userinput = {
    "Country": [Country],
    "EdLevel": [EdLevel],
    "YearsCode": [YearsCode],
    "DevType": [DevType],
    "WorkExp": [WorkExp],
    "RemoteWork": [RemoteWork],
    "OrgSize": [OrgSize],
    "Age": [Age],
    "OpSysProfessional use": [OpSysProfessionalUse],
    "Industry": [Industry],
    "LanguageHaveWorkedWith": [LanguageHaveWorkedWith],
    "JobSatPoints_1": [JobSatPoints_1],
}

DF_UserInput = pd.DataFrame(Userinput)


# ۵. تابع پیش‌بینی
def predict(df):
    prediction = model.predict(df)
    return prediction[0]


# ۶. دکمه پیش‌بینی
if st.button("Predict Salary"):
    try:
        result = predict(DF_UserInput)

        st.markdown(
            f"""
        <div style="
        background:#111827;
        border:1px solid #334155;
        border-radius:20px;
        padding:30px;
        text-align:center;
        margin-top:20px;
        ">

        <p style="color:#94a3b8;margin:0;">
        Estimated Annual Salary
        </p>

        <h1 style="color:#22c55e;">
        ${result:,.0f}
        </h1>

        </div>
        """,
            unsafe_allow_html=True,
        )

        with st.expander("View Submitted Information"):
            st.dataframe(DF_UserInput, use_container_width=True)

    except Exception as e:
        st.error(f"Prediction Error: {str(e)}")
