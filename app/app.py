import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/random_forest_model.pkl")

st.set_page_config(
    page_title="Late Delivery Risk Prediction",
    page_icon="📦"
)

st.title("📦 Late Delivery Risk Prediction")

st.write("Predict whether an order is likely to be delivered late.")

st.header("Enter Order Details")

days_real = st.number_input("Days for shipping (real)", min_value=0, value=3)

days_scheduled = st.number_input(
    "Days for shipment (scheduled)",
    min_value=0,
    value=4
)

benefit = st.number_input(
    "Benefit per order",
    value=25.0
)

sales = st.number_input(
    "Sales per customer",
    value=150.0
)

if st.button("Predict"):

    st.success("🎉 Prediction button is working!")

    st.write("Days for shipping:", days_real)
    st.write("Scheduled days:", days_scheduled)
    st.write("Benefit:", benefit)
    st.write("Sales:", sales)
    