import streamlit as st
import numpy as np
import joblib


model = joblib.load("xgb_model.pkl")

st.set_page_config(page_title="Fraud Detection", page_icon="🛡️")
st.title("🛡️ Online Transaction Fraud Detection")
st.write("Enter transaction details below:")


step = st.number_input("Step (Time Step)", min_value=0)
amount = st.number_input("Transaction Amount", min_value=0.0)
oldbalanceOrg = st.number_input("Old Balance (Origin)", min_value=0.0)
newbalanceOrig = st.number_input("New Balance (Origin)", min_value=0.0)
oldbalanceDest = st.number_input("Old Balance (Destination)", min_value=0.0)
newbalanceDest = st.number_input("New Balance (Destination)", min_value=0.0)


transaction_type = st.selectbox("Transaction Type", ["CASH_OUT", "TRANSFER", "Other"])


type_CASH_OUT = 1 if transaction_type == "CASH_OUT" else 0
type_TRANSFER = 1 if transaction_type == "TRANSFER" else 0


if st.button("Predict"):
    input_data = np.array([[step, amount, oldbalanceOrg, newbalanceOrig,
                            oldbalanceDest, newbalanceDest, type_CASH_OUT, type_TRANSFER]])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("🚨 Fraudulent Transaction Detected!")
    else:
        st.success("✅ This transaction appears to be safe.")














