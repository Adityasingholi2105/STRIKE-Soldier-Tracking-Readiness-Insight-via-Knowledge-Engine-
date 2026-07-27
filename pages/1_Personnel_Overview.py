import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(page_title="Personnel Overview", layout="wide")

# Page title
st.title("👥 Personnel Overview")
st.markdown("Complete overview of all Agniveer personnel in the STRIKE system.")

# Load the dataset
import os
df = pd.read_csv(os.path.join(os.path.dirname(__file__), "..", 'agniveer_data.csv'))

# Top summary metrics - 3 numbers shown side by side
col1, col2, col3 = st.columns(3)

col1.metric("Total Soldiers", len(df))
col2.metric("Avg Fitness Score", round(df["FitnessScore"].mean(), 1))
col3.metric("Avg Age", round(df["Age"].mean(), 1))

# Show the full data table
st.subheader("All Personnel")
st.dataframe(df, use_container_width=True)

# Bar chart - how many soldiers per unit
st.subheader("Soldiers by Unit")
unit_counts = df["Unit"].value_counts().reset_index()
unit_counts.columns = ["Unit", "Count"]
fig = px.bar(unit_counts, x="Unit", y="Count", color="Unit", title="Personnel Distribution by Unit")
st.plotly_chart(fig, use_container_width=True)

