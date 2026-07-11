# 🏦 Bank Term Deposit Subscription Prediction

## 📌 Project Overview

Banks spend significant resources on telemarketing campaigns to promote term deposit products. However, contacting every customer is costly and often results in low conversion rates.

The objective of this project is to build a Machine Learning model that predicts whether a customer is likely to subscribe to a term deposit product. By identifying high-potential customers, banks can improve marketing efficiency, reduce costs, and increase conversion rates.

This project demonstrates an end-to-end Machine Learning workflow including data preprocessing, exploratory data analysis, feature engineering, model building, hyperparameter tuning, model evaluation, explainability, and deployment using Streamlit.

---

## 🎯 Business Problem

Telemarketing campaigns are widely used in the banking industry to promote financial products.

### Challenges

- Large customer base
- Low response rates
- High marketing costs
- Limited targeting capabilities

### Proposed Solution

Develop a predictive model that identifies customers who are more likely to subscribe to a term deposit product, enabling the bank to:

- Focus on high-potential customers
- Improve campaign effectiveness
- Reduce operational costs
- Increase customer conversion rates

---

## 📊 Dataset Information

### Dataset

**Bank Telemarketing Dataset**

Source:

https://www.kaggle.com/datasets/raosuny/success-of-bank-telemarketing-data/data

### Target Variable

| Target | Description |
|----------|-------------|
| Yes | Customer subscribed to term deposit |
| No | Customer did not subscribe |

### Features Used

- Age
- Default Credit Status
- Housing Loan Status
- Personal Loan Status
- Job Category
- Marital Status
- Education Level

---

## ⚙️ Project Workflow

### 1. Business Understanding

- Understand campaign objectives
- Define prediction problem
- Identify target variable

### 2. Data Collection

- Load dataset
- Review structure and attributes

### 3. Data Preprocessing

- Handle missing values
- Remove unnecessary variables
- Encode categorical variables

### 4. Feature Engineering

- One-Hot Encoding
- Feature Selection
- Data Scaling

### 5. Exploratory Data Analysis

- Customer demographics
- Loan distribution
- Subscription trends
- Correlation analysis

### 6. Model Building

Multiple Machine Learning models were trained and evaluated.

### 7. Model Evaluation

Models were evaluated using:

- Accuracy
- Balanced Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score

### 8. Hyperparameter Tuning

Grid Search / Random Search optimization was performed to improve model performance.

### 9. Deployment

The final model was deployed using Streamlit.

---

# 🤖 Machine Learning Models Evaluated

### Model 1 – Baseline Dataset

- Logistic Regression
- Ridge Classifier
- KNN
- Gaussian Naive Bayes
- SVM
- Decision Tree
- Random Forest
- AdaBoost
- Gradient Boosting
- XGBoost

### Model 2 – Feature Engineered Dataset

- Logistic Regression
- Ridge Classifier
- KNN
- Gaussian Naive Bayes
- SVM
- Decision Tree
- Random Forest
- AdaBoost
- Gradient Boosting
- XGBoost

### Model 3 – SMOTE Balanced Dataset

- Logistic Regression
- Ridge Classifier
- KNN
- Gaussian Naive Bayes
- SVM
- Decision Tree
- Random Forest
- AdaBoost
- Gradient Boosting
- XGBoost

### Model 4 – Hyperparameter Tuned Models

- Tuned Logistic Regression
- Tuned Ridge Classifier
- Tuned KNN
- Tuned Gaussian Naive Bayes
- Tuned SVM
- Tuned Decision Tree
- Tuned Random Forest
- Tuned AdaBoost
- Tuned Gradient Boosting
- Tuned XGBoost

---

# 🏆 Final Model Selected

## Gradient Boosting Classifier

The Gradient Boosting Classifier was selected as the final model because it achieved the best overall balance between:

- Balanced Accuracy
- Recall
- F1 Score
- ROC-AUC
- Generalization Capability

### Final Performance Metrics

| Metric | Score |
|----------|---------|
| Train Accuracy | 66.00% |
| Test Accuracy | 66.44% |
| Balanced Accuracy | 58.27% |
| Precision | 18.20% |
| Recall | 47.34% |
| F1 Score | 26.30% |
| ROC-AUC | 60.65% |

---

# 📈 Key Findings

### Important Observations

- Customer demographics influence subscription behavior.
- Loan-related attributes significantly impact decisions.
- Education level provides valuable predictive information.
- Occupation categories affect subscription likelihood.
- SMOTE improved minority class detection.
- Ensemble methods outperformed traditional algorithms.

### Business Insights

- Targeting high-probability customers can significantly improve campaign ROI.
- Predictive analytics can reduce telemarketing costs.
- Customer segmentation enhances campaign effectiveness.

---

# 🖥️ Streamlit Application

The project includes an interactive Streamlit dashboard that allows users to:

### Features

- Customer Profile Input
- Subscription Probability Prediction
- Interactive Gauge Visualization
- Business Recommendation Engine
- Prediction Report Download
- Model Performance Insights

---

## 📷 Application Screenshots

### Home Dashboard

_Add Screenshot Here_

### Prediction Dashboard

_Add Screenshot Here_

### Prediction Results

_Add Screenshot Here_

---

# 🛠️ Technology Stack

### Programming Language

- Python

### Data Processing

- Pandas
- NumPy

### Machine Learning

- Scikit-Learn
- XGBoost

### Visualization

- Plotly
- Matplotlib
- Seaborn

### Deployment

- Streamlit

### Model Serialization

- Joblib

---

# 📂 Project Structure

```text
Bank_Term_Deposit_Project/

│
├── app.py
│
├── gradient_boosting_model.pkl
├── scaler.pkl
├── feature_columns.pkl
│
├── requirements.txt
├── README.md
│
└── assets/
```

---

# 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/bank-term-deposit-subscription-predictor.git
```

### Navigate to Project Folder

```bash
cd bank-term-deposit-subscription-predictor
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

# 🌐 Live Demo

### Streamlit Application

```
Add Streamlit URL Here
```

### GitHub Repository

```
Add GitHub Repository URL Here
```

---

# 📚 Future Scope

### Potential Enhancements

- Incorporate customer behavioral data
- Real-time prediction pipelines
- Cloud deployment
- Customer segmentation engine
- Automated campaign recommendation system
- Integration with CRM platforms
- Advanced ensemble models such as LightGBM and CatBoost

---

# 👨‍💻 Author

**Nakul**

Data Analytics & Machine Learning Project

---

# ⭐ If you found this project useful

Please consider giving this repository a star.