import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

st.title("🔥 ML Prediction Test")

try:
    data = {
        "FitnessScore": [85, 92, 70, 65, 90, 55],
        "Age": [30, 45, 35, 25, 40, 50],
        "YearsOfService": [10, 15, 5, 7, 20, 3],
        "PromotionEligible": ["Yes", "Yes", "No", "No", "Yes", "No"]
    }
    df = pd.DataFrame(data)
    df["PromotionBinary"] = df["PromotionEligible"].map({"Yes": 1, "No": 0})

    X = df[["FitnessScore", "Age", "YearsOfService"]]
    y = df["PromotionBinary"]
    model = LogisticRegression()
    model.fit(X, y)
    st.success("✅ ML model trained successfully.")
except Exception as e:
    st.error(f"❌ Error: {e}")
