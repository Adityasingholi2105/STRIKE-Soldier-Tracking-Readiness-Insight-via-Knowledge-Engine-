import os

import pandas as pd
import plotly.express as px
import streamlit as st

from utils.styles import apply_theme

st.set_page_config(page_title="Personnel Overview", layout="wide")
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

st.title("Personnel Overview")
st.markdown("Complete overview of all Agniveer personnel in the STRIKE system.")

df = pd.read_csv(os.path.join(os.path.dirname(__file__), "..", "agniveer_data.csv"))

col1, col2, col3 = st.columns(3)
col1.metric("Total Soldiers", len(df))
col2.metric("Avg Fitness Score", round(df["FitnessScore"].mean(), 1))
col3.metric("Avg Age", round(df["Age"].mean(), 1))

st.subheader("All Personnel")
st.dataframe(df, width="stretch")

st.subheader("Soldiers by Unit")
unit_counts = df["Unit"].value_counts().reset_index()
unit_counts.columns = ["Unit", "Count"]
fig = px.bar(
    unit_counts,
    x="Unit",
    y="Count",
    color="Unit",
    title="Personnel Distribution by Unit",
    color_discrete_sequence=["#4ade80", "#22c55e", "#16a34a", "#15803d", "#166534"],
)
fig.update_layout(paper_bgcolor="#080c14", plot_bgcolor="#0d1117", font_color="#c9d1d9")
st.plotly_chart(fig, width="stretch")
