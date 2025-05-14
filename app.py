import streamlit as st
import numpy as np
model = joblib.load("xgboost_model (2).pkl"
st.title("🛡️ Online Transaction Fraud Detection")
st.write("Fill in transaction details to detect if it's fraudulent.")

step = st.number_input("Step", min_value=0)
amount = st.number_input("Amount", min_value=0.0)
oldbalanceOrg = st.number_input("Old Balance (Origin)", min_value=0.0)
newbalanceOrig = st.number_input("New Balance (Origin)", min_value=0.0)
oldbalanceDest = st.number_input("Old Balance (Destination)", min_value=0.0)

if st.button("Predict"):
    input_data = np.array([[step, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest]])
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("🚨 Fraud Detected!")
    else:
        st.success("✅ Safe Transaction")

