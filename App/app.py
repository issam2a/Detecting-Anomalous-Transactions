import streamlit as st
import pandas as pd
import joblib
import os 

def feature_engineering(X):
    X = X.copy()
    # Example features you added
    X['diffOrig'] = X['oldbalanceOrg'] - X['newbalanceOrig']
    X['diffDest'] = X['newbalanceDest'] - X['oldbalanceDest']
    X['amt_ratio'] = X['amount'] / (X['oldbalanceOrg'] + 1)
    X['is_suspicious_type'] = X['type'].isin(['TRANSFER', 'CASH_OUT']).astype(int)
    return X

# Get the folder where app.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load trained pipeline
pipeline = joblib.load(os.path.join(BASE_DIR, "fraud_detection_model.pkl"))

st.set_page_config(page_title="Fraud Detection App", page_icon="💳", layout="centered")

st.title("💳 Fraud Detection App")
st.write("Enter transaction details below and check if it's **Fraudulent** or **Legit**.")

# Form for user input
with st.form("fraud_form"):
    step = st.number_input("Step (time step of transaction)", min_value=1, max_value=1000000, value=500)
    type_ = st.selectbox("Transaction Type", ["TRANSFER", "CASH_OUT", "PAYMENT", "DEBIT"])
    amount = st.number_input("Transaction Amount", min_value=0.0, value=1000.0, step=100.0)
    
    oldbalanceOrg = st.number_input("Old Balance (Origin)", min_value=0.0, value=5000.0, step=100.0)
    newbalanceOrg = st.number_input("New Balance (Origin)", min_value=0.0, value=4000.0, step=100.0)
    
    oldbalanceDest = st.number_input("Old Balance (Destination)", min_value=0.0, value=0.0, step=100.0)
    newbalanceDest = st.number_input("New Balance (Destination)", min_value=0.0, value=0.0, step=100.0)

    submitted = st.form_submit_button("🔍 Predict")

if submitted:
    # Create transaction as DataFrame
    transaction = pd.DataFrame([{
        'step': step,
        'type': type_,
        'amount': amount,
        'nameOrig': "C123456789",   # placeholders
        'oldbalanceOrg': oldbalanceOrg,
        'newbalanceOrig': newbalanceOrg,
        'nameDest': "M987654321",
        'oldbalanceDest': oldbalanceDest,
        'newbalanceDest': newbalanceDest,
        'isFraud': 0,
        'isFlaggedFraud': 0
    }])

    # Predict
    prediction = pipeline.predict(transaction)[0]
    probability = pipeline.predict_proba(transaction)[:, 1][0]

    # Show result
    st.subheader("🔎 Result")
    if prediction == 1:
        st.error(f"⚠️ FRAUD detected! Probability: {probability:.2%}")
    else:
        st.success(f"✅ Legit Transaction. Fraud Probability: {probability:.2%}")
