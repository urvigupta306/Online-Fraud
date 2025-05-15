import streamlit as st
import numpy as np
import joblib

model = joblib.load("xgb_model.pkl")
import streamlit as st
import numpy as np
import joblib


model = joblib.load("xgb_model.pkl")


st.title("🛡️ Online Transaction Fraud Detection")
st.write("Fill in transaction details to detect if it's fraudulent.")

# Input fields
step = st.number_input("Step", min_value=0)
amount = st.number_input("Transaction Amount", min_value=0.0)
oldbalanceOrg = st.number_input("Old Balance (Origin)", min_value=0.0)
newbalanceOrig = st.number_input("New Balance (Origin)", min_value=0.0)
oldbalanceDest = st.number_input("Old Balance (Destination)", min_value=0.0)
newbalanceDest = st.number_input("New Balance (Destination)", min_value=0.0)

transaction_type = st.selectbox("Transaction Type", ["TRANSFER", "CASH_OUT"])


if transaction_type == "TRANSFER":
    transfer = 1
    cash_out = 0
else:  
    transfer = 0
    cash_out = 1


if st.button("Predict"):
    input_data = np.array([[step, amount, oldbalanceOrg, newbalanceOrig,
                            oldbalanceDest, newbalanceDest,
                            transfer, cash_out]])
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("🚨 Fraud Detected!")
    else:
        st.success("✅ Safe Transaction")








