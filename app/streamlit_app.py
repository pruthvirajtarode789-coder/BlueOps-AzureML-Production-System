# app/streamlit_app.py
import streamlit as st
import requests
import os

st.set_page_config(layout="wide", page_title="BlueOps - Analytics")

API_URL = "https://blueops-api.onrender.com"

st.title("🔵 BlueOps — ML Production Demo")
st.markdown("Model endpoint: " + API_URL)

st.sidebar.header("Prediction")
f1 = st.sidebar.number_input("Feature 1", value=0.0, format="%.4f")
f2 = st.sidebar.number_input("Feature 2", value=0.0, format="%.4f")
f3 = st.sidebar.number_input("Feature 3", value=0.0, format="%.4f")

if st.sidebar.button("Predict"):
    payload = {"feature_1": float(f1), "feature_2": float(f2), "feature_3": float(f3)}
    try:
        r = requests.post(API_URL + "/predict", json=payload, timeout=10)
        if r.status_code == 200:
            data = r.json()
            st.success(f"Prediction: {data['prediction']} — Prob: {data['probability']:.3f}")
        else:
            st.error("API error: " + r.text)
    except Exception as e:
        st.error("Connection error: " + str(e))

st.markdown("---")
st.markdown("## Quick notes")
st.write("- Train with `python training/train_model.py`")
st.write("- API at `/predict` returns JSON `{prediction, probability}`")
