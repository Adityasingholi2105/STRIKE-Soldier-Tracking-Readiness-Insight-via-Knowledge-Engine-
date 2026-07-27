import streamlit as st 
import pandas as pd 
import plotly.express as px 
from personnel_analyzer import calculate_readiness_status, analyze_unit_fitness

st.set_page_config(page_title="Readiness Analytics", layout="wide")

st.title("📊 Readiness Analytics")
st.markdown("Fitness and readiness breakdown across all Agniveer personnel.")

#Load data and calculate readiness
import os
df = pd.read_csv(os.path.join(os.path.dirname(__file__), "..", "agniveer_data.csv"))
ddf = calculate_readiness_status(df)

#Summary metrics 
col1, col2, col3 = st.columns(3)

col1.metric("Fit", len(df[df["ReadinessStatus"] == "Fit"]))
col2.metric("watchlist", len(df[df["ReadinessStatus"] == "Watchlist"]))
col3.metric("Unfit",len(df[df["ReadinessStatus"] =="Unfit"]))

#Pie chart - readiness distribution
st.subheader("Readiness Distribution")
readiness_counts = df["ReadinessStatus"].value_counts().reset_index()
readiness_counts.colums = ["Status", "Count"]
fig = px.pie(readiness_counts, names="ReadinessStatus", values="count",
             title="Personnel Readiness Stauts",
             color_discrete_map={"Fit": "green", "Watchlist": "orange", "Unfit": "red"})
st.plotly_chart(fig, use_container_width=True)

#unite wise fitness table 
st.subheader("Unit-wise Fitness Analysis")
unit_fitness = analyze_unit_fitness(df)
st.dataframe(unit_fitness, use_container_width=True)

# Bar chart - average fitness by unit 
st.subheader("Average Fitness Score by Uint")
unit_fitness_reset = unit_fitness.reset_index()
fig2 = px.bar(unit_fitness_reset, x="Unit", y="Avg_Fitness",
              color="Unit", title="Average Fitness Per Unit")
st.plotly_chart(fig2, use_container_width=True)

