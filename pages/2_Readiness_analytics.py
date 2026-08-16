import os

import pandas as pd
import plotly.express as px
import streamlit as st

from personnel_analyzer import analyze_unit_fitness, calculate_readiness_status
from utils.styles import apply_theme

st.set_page_config(page_title="Readiness Analytics", layout="wide")
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

st.title("Readiness Analytics")
st.markdown("Readiness posture across all units and personnel categories.")

df = pd.read_csv(os.path.join(os.path.dirname(__file__), "..", "agniveer_data.csv"))
df = calculate_readiness_status(df)

col1, col2, col3 = st.columns(3)
col1.metric("Fit", int((df["ReadinessStatus"] == "Fit").sum()))
col2.metric("Watchlist", int((df["ReadinessStatus"] == "Watchlist").sum()))
col3.metric("Unfit", int((df["ReadinessStatus"] == "Unfit").sum()))

st.subheader("Readiness Distribution")
readiness_counts = df["ReadinessStatus"].value_counts().reset_index()
readiness_counts.columns = ["Status", "Count"]
fig = px.pie(
    readiness_counts,
    names="Status",
    values="Count",
    title="Personnel Readiness Status",
    color_discrete_map={"Fit": "#4ade80", "Watchlist": "#fbbf24", "Unfit": "#f87171"},
)
fig.update_layout(paper_bgcolor="#080c14", plot_bgcolor="#0d1117", font_color="#c9d1d9")
st.plotly_chart(fig, width="stretch")

st.subheader("Unit-wise Fitness Analysis")
unit_fitness = analyze_unit_fitness(df)
st.dataframe(unit_fitness, width="stretch")

st.subheader("Average Fitness Score by Unit")
unit_fitness_reset = unit_fitness.reset_index()
fig2 = px.bar(unit_fitness_reset, x="Unit", y="Avg_Fitness", color="Unit", title="Average Fitness Per Unit")
fig2.update_layout(paper_bgcolor="#080c14", plot_bgcolor="#0d1117", font_color="#c9d1d9")
st.plotly_chart(fig2, width="stretch")

