import streamlit as st 
import pandas as pd 
import pickle
import os 

st.set_page_config(page_title="Retention Predictor", layout="wide")

st.title("Agniveer Retention Risk Predictor")
st.markdown("Predict which Agniveer are likely to be retained after their 4-year tenure.")

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), "..", "models", "retention_model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

#load the data 
data_path = os.path.join(os.path.dirname(__file__), "..", "agniveer_data.csv")
df = pd.read_csv(data_path)

# Two section - bulk prediction and individual predictio 
tab1, tab2, = st.tabs(["Bulk Prediction", "Individual Soldier"])

with tab1:
    st.subheader("Retention Prediction for All Personnel")
    
    # Run the prediction on all soldiers 
    features = ["FitnessScore", "TrainingScore", "PhysicalTestPass", "DisciplinaryRecord", "FitnessTrend", "TenureYears"]
    df["PredictionRetention"] = model.predict(df[features])
    df["RetentionLabel"] = df["PredictionRetention"].map({1: "Retained", 0: "Exit"})

    #show summary metrics 
    col1, col2, = st.columns(2)
    col1.metric("Predicted Retained", int(df["PredictionRetention"].sum()))
    col2.metric("Predicted Exit", int((df["PredictionRetention"] == 0).sum()))
    
    #Show Full table 
    st.dataframe(df[["ID", "Name", "FitnessScore", "TrainingScore", "TenureYears", "RetentionLabel"]], use_container_width=True)

with tab2:
    st.subheader("Predict for Individual Soldier")

    col1, col2 = st.columns(2)

    with col1:
        fitness = st.slider("Fitness Score", 50, 100, 75)
        training = st.slider("Training Score", 40, 100, 70)
        tenure = st.slider("Tenure Year(1-4)", 1, 4, 2)
    
    with col2:
        physical = st.selectbox("Physical Test Pass", [1, 0], format_func=lambda x: "Yes" if x == 1 else "No")
        discipplinary = st.selectbox("Disciplinary Record", [0, 1], format_func=lambda x: "Clean" if x == 0 else "Has Record")
        trend = st.selectbox("Fitness Trend", [1, 0], format_func=lambda x: "Improving" if x == 1 else "Declining")

        # Predict button 
        if st.button("Predict Retention"):
            input_data = pd.DataFrame([[fitness, training, physical, discipplinary, trend, tenure]],
                                      columns=["FitnessScore", "TrainingScore", "PhysicalTestPass",
                                               "DisciplinaryRecord", "FitnessTrend", "TenureYears"])
            prediction = model.predict(input_data)[0]
            probability = model.predict_proba(input_data)[0]

            if prediction == 1:
                st.success(f"This Soldier is likely to be RETAINED (Confidence: {probability[1]*100:.1f}%)")
            else:
                st.error(f" This Soldier is likely to EXIT after tenure (Confidence: {probability[0]*100:.1f}%)")

 













