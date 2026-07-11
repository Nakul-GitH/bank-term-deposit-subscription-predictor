# ==========================================================
# Bank Term Deposit Subscription Predictor
# Final Production Ready Streamlit Application
# ==========================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Bank Term Deposit Predictor",
    page_icon="🏦",
    layout="wide"
)

# ==========================================================
# LOAD MODEL FILES
# ==========================================================

model = joblib.load("gradient_boosting_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_columns = joblib.load("feature_columns.pkl")

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.main {
    background-color: #F8FAFC;
}

[data-testid="stSidebar"] {
    background-color: #0F172A;
}

[data-testid="stSidebar"] * {
    color: white;
}

.big-title {
    font-size:40px;
    font-weight:700;
    color:#0F172A;
}

.sub-title {
    font-size:18px;
    color:#475569;
}

.metric-card {
    background-color:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.1);
    text-align:center;
}

.metric-title {
    font-size:16px;
    color:#64748B;
}

.metric-value {
    font-size:28px;
    font-weight:bold;
    color:#1E40AF;
}

.prediction-card {
    padding:25px;
    border-radius:15px;
    text-align:center;
    color:white;
    font-size:26px;
    font-weight:bold;
}

.footer {
    text-align:center;
    color:#64748B;
    font-size:14px;
    margin-top:30px;
}

.recommendation {
    background:#FFFFFF;
    padding:20px;
    border-radius:15px;
    border-left:8px solid #1E40AF;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.markdown("## 🏦 Bank Subscription Predictor")

st.sidebar.markdown("---")

st.sidebar.markdown("### 🤖 Model Information")

st.sidebar.info("""
**Selected Model**

Gradient Boosting Classifier
""")

st.sidebar.markdown("### 📊 Model Performance")

st.sidebar.success("""
Balanced Accuracy : 58.27%

Recall : 47.34%

F1 Score : 26.30%

ROC-AUC : 60.65%
""")

st.sidebar.markdown("---")

st.sidebar.markdown("""
### 📁 Project Details

Dataset:
Bank Telemarketing Dataset

Features Used:
19

Target:
Term Deposit Subscription
""")

# ==========================================================
# HEADER
# ==========================================================

st.markdown(
    """
    <div class='big-title'>
    🏦 Bank Term Deposit Subscription Predictor
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='sub-title'>
    Machine Learning Powered Customer Subscription Intelligence System
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ==========================================================
# KPI CARDS
# ==========================================================

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class='metric-card'>
        <div class='metric-title'>Balanced Accuracy</div>
        <div class='metric-value'>58.27%</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='metric-card'>
        <div class='metric-title'>Recall</div>
        <div class='metric-value'>47.34%</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='metric-card'>
        <div class='metric-title'>F1 Score</div>
        <div class='metric-value'>26.30%</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class='metric-card'>
        <div class='metric-title'>ROC-AUC</div>
        <div class='metric-value'>60.65%</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ==========================================================
# CUSTOMER INPUT SECTION
# ==========================================================

st.subheader("📋 Customer Information")

col1,col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=35
    )

    default_credit = st.selectbox(
        "Default Credit",
        ["No","Yes"]
    )

    housing_loan = st.selectbox(
        "Housing Loan",
        ["No","Yes"]
    )

    personal_loan = st.selectbox(
        "Personal Loan",
        ["No","Yes"]
    )

with col2:

    job = st.selectbox(
        "Job",
        [
            "admin.",
            "blue-collar",
            "entrepreneur",
            "housemaid",
            "management",
            "retired",
            "self-employed",
            "services",
            "student",
            "technician",
            "unemployed"
        ]
    )

    marital = st.selectbox(
        "Marital Status",
        [
            "divorced",
            "married",
            "single"
        ]
    )

    education = st.selectbox(
        "Education",
        [
            "Primary Education",
            "Professional Education",
            "Secondary Education",
            "Tertiary Education"
        ]
    )

# ==========================================================
# FEATURE CREATION
# ==========================================================

def create_feature_vector():

    row = dict.fromkeys(feature_columns,0)

    row["Age"] = age

    row["Default_Credit"] = 1 if default_credit=="Yes" else 0
    row["Housing_Loan"] = 1 if housing_loan=="Yes" else 0
    row["Personal_Loan"] = 1 if personal_loan=="Yes" else 0

    # Job Encoding

    if job != "admin.":
        col = f"Job_{job}"
        if col in row:
            row[col] = 1

    # Marital Status

    if marital == "married":
        row["Marital_Status_married"] = 1

    elif marital == "single":
        row["Marital_Status_single"] = 1

    # Education

    if education == "Professional Education":
        row["Education_Professional_Education"] = 1

    elif education == "Secondary Education":
        row["Education_Secondary_Education"] = 1

    elif education == "Tertiary Education":
        row["Education_Tertiary_Education"] = 1

    return pd.DataFrame([row])

# ==========================================================
# PREDICTION BUTTON
# ==========================================================

if st.button("🔍 Predict Subscription Probability"):

    input_df = create_feature_vector()

    scaled_input = scaler.transform(input_df)

    prediction = model.predict(scaled_input)[0]

    probability = model.predict_proba(scaled_input)[0][1]

    st.write("")
    st.write("")

    # ======================================================
    # PREDICTION OUTPUT
    # ======================================================

    if probability >= 0.50:

        st.markdown(
            """
            <div class='prediction-card'
            style='background:#22C55E;'>
            ✅ Likely to Subscribe
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            """
            <div class='prediction-card'
            style='background:#EF4444;'>
            ❌ Unlikely to Subscribe
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")
    st.write("")

    # ======================================================
    # PROBABILITY
    # ======================================================

    st.subheader("📈 Subscription Probability")

    st.progress(float(probability))

    st.metric(
        "Predicted Probability",
        f"{probability*100:.2f}%"
    )

    # ======================================================
    # RECOMMENDATION ENGINE
    # ======================================================

    st.write("")
    st.subheader("💡 Business Recommendation")

    if probability >= 0.70:

        st.markdown("""
        <div class='recommendation'>
        <h4>🟢 High Probability Customer</h4>

        Recommended Action:

        • Include in immediate marketing campaign

        • High conversion potential

        • Priority lead for sales outreach
        </div>
        """, unsafe_allow_html=True)

    elif probability >= 0.40:

        st.markdown("""
        <div class='recommendation'>
        <h4>🟡 Medium Probability Customer</h4>

        Recommended Action:

        • Include in secondary campaign

        • Consider personalized communication

        • Follow-up marketing suggested
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div class='recommendation'>
        <h4>🔴 Low Probability Customer</h4>

        Recommended Action:

        • Do not prioritize immediately

        • Focus marketing budget elsewhere

        • Re-evaluate in future campaigns
        </div>
        """, unsafe_allow_html=True)

# ==========================================================
# FOOTER
# ==========================================================

st.write("")
st.write("")
st.markdown("""
<div class='footer'>

Developed using Machine Learning

Gradient Boosting Classifier | Streamlit Deployment

Bank Term Deposit Subscription Prediction Project

</div>
""", unsafe_allow_html=True)