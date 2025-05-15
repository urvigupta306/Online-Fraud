import streamlit as st
import numpy as np
import joblib


model = joblib.load("xgb_model.pkl")


st.title("🛡️ Online Transaction Fraud Detection")
st.write("Fill in transaction details to detect if it's fraudulent.")

import pandas as pd

if st.button("Predict"):
    input_dict = {

step = st.number_input("Step", min_value=0)
amount = st.number_input("Transaction Amount", min_value=0.0)
oldbalanceOrg = st.number_input("Old Balance (Origin)", min_value=0.0)
newbalanceOrig = st.number_input("New Balance (Origin)", min_value=0.0)
oldbalanceDest = st.number_input("Old Balance (Destination)", min_value=0.0)
newbalanceDest = st.number_input("New Balance (Destination)", min_value=0.0)

    }

    input_df = pd.DataFrame(input_dict)

    try:
        prediction = model.predict(input_df)[0]
        if prediction == 1:
            st.error("🚨 Fraud Detected!")
        else:
            st.success("✅ Safe Transaction")
    except Exception as e:
        st.error(f"Prediction failed: {e}")










