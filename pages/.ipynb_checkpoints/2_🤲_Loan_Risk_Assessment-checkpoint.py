import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

st.title("🤲 Loan Risk Assessment")

def loan_risk_assessment():
    loan_amount = st.number_input("Loan Amount (USD)", min_value=1000, value=5000, step=500)
    loan_term = st.slider("Loan Term (Years)", 1, 30, 10)
    interest_rate = st.slider("Interest Rate (%)", 0.0, 15.0, 5.0)
    credit_score = st.slider("Credit Score", 300, 850, 700)
    annual_income = st.number_input("Annual Income (USD)", min_value=0, value=50000, step=1000)
    monthly_debt = st.number_input("Monthly Debt Payments (USD)", min_value=0, value=500, step=50)

    def predict_loan_risk(credit_score, debt_to_income_ratio):
        if credit_score < 580 or debt_to_income_ratio > 0.5:
            return "High Risk"
        elif 580 <= credit_score <= 700 or 0.3 <= debt_to_income_ratio <= 0.5:
            return "Medium Risk"
        else:
            return "Low Risk"

    debt_to_income_ratio = (monthly_debt * 12) / (annual_income + 1e-9)
    loan_risk = predict_loan_risk(credit_score, debt_to_income_ratio)

    st.write(f"Loan Amount: ${loan_amount:,.2f}")
    st.write(f"Loan Term: {loan_term} years @ {interest_rate:.2f}%")
    st.write(f"Debt-to-Income Ratio: {debt_to_income_ratio:.2f}")
    st.write(f"Credit Score: {credit_score}")
    st.subheader(f"🔮 Predicted Loan Risk: **{loan_risk}**")

loan_risk_assessment()
