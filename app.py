import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load sample data (replace this with your actual data)
def load_data():
    data = pd.read_csv('sample_loan_data.csv')  # Ensure your data is in this file
    return data

# Train a simple RandomForest model (replace this with your actual model training)
def train_model(data):
    X = data.drop(columns=['FinalRiskLevel'])
    y = data['FinalRiskLevel']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return model, accuracy

# Predict function
def predict(model, input_data):
    prediction = model.predict(input_data)
    return prediction

# Streamlit app
def main():
    st.title("Loan Approval Prediction")

    # Input fields
    Gender = st.selectbox("Gender", ["Male", "Female"])
    Age = st.number_input("Age", min_value=18, max_value=100, value=30)
    MaritalStatus = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
    Type = st.selectbox("Type", ["Personal", "Business"])
    BusinessOwner = st.selectbox("Business Owner", ["Yes", "No"])
    BusinessExpYear = st.number_input("Business Experience (Years)", min_value=0, max_value=50, value=0)
    HaveMobileNo = st.selectbox("Have Mobile No", ["Yes", "No"])
    AppliedAmount = st.number_input("Applied Amount", min_value=0, value=10000)
    TotalCreditAmount = st.number_input("Total Credit Amount", min_value=0, value=20000)
    TotalIncome = st.number_input("Total Income", min_value=0, value=50000)
    TotalDebt = st.number_input("Total Debt", min_value=0, value=10000)
    Installment = st.number_input("Installment", min_value=0, value=2000)
    CollateralFlag = st.selectbox("Collateral Flag", ["Yes", "No"])
    TenorLoan1 = st.number_input("Tenor Loan 1", min_value=1, max_value=360, value=12)
    Score = st.number_input("Score", min_value=300, max_value=850, value=700)

    # Create input dataframe
    input_data = pd.DataFrame({
        'Gender': [Gender],
        'Age': [Age],
        'MaritalStatus': [MaritalStatus],
        'Type': [Type],
        'BusinessOwner': [BusinessOwner],
        'BusinessExpYear': [BusinessExpYear],
        'HaveMobileNo': [HaveMobileNo],
        'AppliedAmount': [AppliedAmount],
        'TotalCreditAmount': [TotalCreditAmount],
        'TotalIncome': [TotalIncome],
        'TotalDebt': [TotalDebt],
        'Installment': [Installment],
        'CollateralFlag': [CollateralFlag],
        'TenorLoan1': [TenorLoan1],
        'Score': [Score]
    })

    # Load data and train model
    data = load_data()
    model, accuracy = train_model(data)

    if st.button("Predict"):
        prediction = predict(model, input_data)
        st.write(f"The predicted Final Risk Level is: {prediction[0]}")
        st.write(f"Model Accuracy: {accuracy * 100:.2f}%")

if __name__ == "__main__":
    main()
