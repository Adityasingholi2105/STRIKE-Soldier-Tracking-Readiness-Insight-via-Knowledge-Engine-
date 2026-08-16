import streamlit as st
from utils.styles import apply_theme


st.set_page_config(page_title="STRIKE Dashboard", layout="wide")
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

st.title("STRIKE Dashboard")
st.markdown(
    """
    <div style="margin-top: 0.5rem; margin-bottom: 1.5rem; font-size: 1.15rem; color: #9aa5b1; letter-spacing: 0.02em;">
        Mission readiness and personnel insights across the force.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div style="background: linear-gradient(135deg, rgba(20, 32, 46, 0.95), rgba(9, 17, 25, 0.96));
                border: 1px solid #2b3a45; border-radius: 18px; padding: 1.5rem 1.7rem; margin-bottom: 1.5rem;">
        <div style="font-size: 0.82rem; color: #4ade80; letter-spacing: 0.12em; text-transform: uppercase; font-weight: 700; margin-bottom: 0.8rem;">
            What this project does
        </div>
        <div style="font-size: 1.05rem; line-height: 1.75; color: #dfe7ef;">
            <strong style="color: #f3f6f8;">STRIKE</strong> is a defense analytics platform designed to track soldiers, monitor readiness, and support decision-making across a unit or force.
            It brings together personnel data, fitness trends, and predictive intelligence to help commanders understand who is mission-ready,
            who needs intervention, and which soldiers are at risk of attrition.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

cols = st.columns(3)
with cols[0]:
    st.markdown(
        """
        <div style="background: rgba(13,17,23,0.95); border: 1px solid #30363d; border-radius: 14px; padding: 1.2rem; height: 100%;">
            <div style="font-size: 0.72rem; color: #4ade80; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; margin-bottom: 0.7rem;">Personnel tracking</div>
            <div style="font-size: 1.05rem; color: #e6edf3; line-height: 1.6;">
                Keep a clear view of soldier records, unit distribution, age, rank, and fitness profiles in one place.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with cols[1]:
    st.markdown(
        """
        <div style="background: rgba(13,17,23,0.95); border: 1px solid #30363d; border-radius: 14px; padding: 1.2rem; height: 100%;">
            <div style="font-size: 0.72rem; color: #4ade80; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; margin-bottom: 0.7rem;">Readiness analytics</div>
            <div style="font-size: 1.05rem; color: #e6edf3; line-height: 1.6;">
                Analyze fitness health, readiness status, and unit-level performance to identify gaps before they become operational risks.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with cols[2]:
    st.markdown(
        """
        <div style="background: rgba(13,17,23,0.95); border: 1px solid #30363d; border-radius: 14px; padding: 1.2rem; height: 100%;">
            <div style="font-size: 0.72rem; color: #4ade80; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; margin-bottom: 0.7rem;">Retention insight</div>
            <div style="font-size: 1.05rem; color: #e6edf3; line-height: 1.6;">
                Use predictive modeling to estimate retention likelihood and detect soldiers who may require intervention or support.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
