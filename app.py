import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
def load_model():
    with open('predict.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

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
    FinalRiskLevel = st.selectbox("Final Risk Level", ["Low", "Medium", "High"])

    # Convert categorical data to numeric data
    input_data = pd.DataFrame({
        'Gender': [1 if Gender == "Male" else 0],
        'Age': [Age],
        'MaritalStatus': [1 if MaritalStatus == "Married" else 0],
        'Type': [1 if Type == "Business" else 0],
        'BusinessOwner': [1 if BusinessOwner == "Yes" else 0],
        'BusinessExpYear': [BusinessExpYear],
        'HaveMobileNo': [1 if HaveMobileNo == "Yes" else 0],
        'AppliedAmount': [AppliedAmount],
        'TotalCreditAmount': [TotalCreditAmount],
        'TotalIncome': [TotalIncome],
        'TotalDebt': [TotalDebt],
        'Installment': [Installment],
        'CollateralFlag': [1 if CollateralFlag == "Yes" else 0],
        'TenorLoan1': [TenorLoan1],
        'Score': [Score],
        'FinalRiskLevel': [0 if FinalRiskLevel == "Low" else (1 if FinalRiskLevel == "Medium" else 2)]
    })

    # Load model
    model = load_model()

    if st.button("Predict"):
        prediction = predict(model, input_data)
        st.write(f"The predicted Loan Status is: {prediction[0]}")

if __name__ == "__main__":
    main()
