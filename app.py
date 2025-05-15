import streamlit as st
import numpy as np
import joblib

model = joblib.load("xgb_model.pkl")


import pandas as pd

if st.button("Predict"):
    input_dict = {
        'step': [step],
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrig': [newbalanceOrig],
        'oldbalanceDest': [oldbalanceDest],
        'newbalanceDest': [newbalanceDest],
        'TRANSFER': [transfer],
        'CASH_OUT': [cash_out]
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






