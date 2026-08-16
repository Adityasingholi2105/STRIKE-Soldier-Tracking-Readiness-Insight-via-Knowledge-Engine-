import os
import pickle

import pandas as pd
import streamlit as st

from utils.styles import apply_theme

st.set_page_config(page_title="Retention Predictor", layout="wide")
apply_theme()

st.sidebar.markdown(
    """
    <div style='padding: 1.5rem 0.5rem 2rem 0.5rem; border-bottom: 1px solid #30363d; margin-bottom: 1rem;'>
        <div style='font-size: 1.4rem; font-weight: 700; color: #4ade80; letter-spacing: 0.08em;'>STRIKE</div>
        <div style='font-size: 0.7rem; color: #6e7681; margin-top: 0.3rem; letter-spacing: 0.1em; text-transform: uppercase;'>Defense Analytics Platform</div>
        <div style='margin-top: 0.8rem;'>
            <span style='font-size: 0.7rem; color: #4ade80; letter-spacing: 0.05em;'>&#9679; SYSTEM ACTIVE</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.title("Retention Predictor")
st.markdown("Forecast retention risk and identify soldiers who may exit after their current tenure.")

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), "..", "models", "retention_model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

# load the data
data_path = os.path.join(os.path.dirname(__file__), "..", "agniveer_data.csv")
df = pd.read_csv(data_path)

# Two section - bulk prediction and individual prediction
tab1, tab2 = st.tabs(["Bulk Prediction", "Individual Soldier"])

with tab1:
    st.subheader("Retention Prediction for All Personnel")

    # Run the prediction on all soldiers
    features = ["FitnessScore", "TrainingScore", "PhysicalTestPass", "DisciplinaryRecord", "FitnessTrend", "TenureYears"]
    df["PredictionRetention"] = model.predict(df[features])
    df["RetentionLabel"] = df["PredictionRetention"].map({1: "Retained", 0: "Exit"})

    # show summary metrics
    col1, col2 = st.columns(2)
    col1.metric("Predicted Retained", int(df["PredictionRetention"].sum()))
    col2.metric("Predicted Exit", int((df["PredictionRetention"] == 0).sum()))

    # Show Full table
    st.dataframe(df[["ID", "Name", "FitnessScore", "TrainingScore", "TenureYears", "RetentionLabel"]], width="stretch")

with tab2:
    st.subheader("Predict for Individual Soldier")

    col1, col2 = st.columns(2)

    with col1:
        fitness = st.slider("Fitness Score", 50, 100, 75)
        training = st.slider("Training Score", 40, 100, 70)
        tenure = st.slider("Tenure Year (1-4)", 1, 4, 2)

    with col2:
        physical = st.selectbox("Physical Test Pass", [1, 0], format_func=lambda x: "Yes" if x == 1 else "No")
        disciplinary = st.selectbox("Disciplinary Record", [0, 1], format_func=lambda x: "Clean" if x == 0 else "Has Record")
        trend = st.selectbox("Fitness Trend", [1, 0], format_func=lambda x: "Improving" if x == 1 else "Declining")

        if st.button("Predict Retention"):
            input_data = pd.DataFrame(
                [[fitness, training, physical, disciplinary, trend, tenure]],
                columns=["FitnessScore", "TrainingScore", "PhysicalTestPass", "DisciplinaryRecord", "FitnessTrend", "TenureYears"],
            )
            prediction = model.predict(input_data)[0]
            probability = model.predict_proba(input_data)[0]

            if prediction == 1:
                st.success(f"This Soldier is likely to be RETAINED (Confidence: {probability[1] * 100:.1f}%)")
            else:
                st.error(f"This Soldier is likely to EXIT after tenure (Confidence: {probability[0] * 100:.1f}%)")


