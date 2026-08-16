import streamlit as st


def apply_theme():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap');

        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {display: none;}

        html, body, [class*="css"] {
            font-family: 'Space Grotesk', sans-serif;
            background-color: #080c14;
            color: #c9d1d9;
        }

        [data-testid="stSidebar"] {
            background-color: #0d1117;
            border-right: 1px solid #30363d;
        }

        [data-testid="stSidebarNav"] a {
            color: #8b949e !important;
            font-size: 0.88rem;
            font-weight: 500;
            letter-spacing: 0.03em;
            padding: 0.6rem 1rem;
            border-radius: 6px;
        }

        [data-testid="stSidebarNav"] a:hover {
            color: #4ade80 !important;
            background-color: #161b22;
        }

        [data-testid="stSidebarNav"] a[aria-current="page"] {
            color: #4ade80 !important;
            background-color: #161b22;
            border-left: 3px solid #4ade80;
        }

        .main .block-container {
            padding: 2rem 3rem;
            background-color: #080c14;
        }

        [data-testid="metric-container"] {
            background: linear-gradient(135deg, #0d1117 0%, #161b22 100%);
            border: 1px solid #30363d;
            border-radius: 10px;
            padding: 1.2rem 1.5rem;
            box-shadow: 0 0 20px rgba(74, 222, 128, 0.05);
        }

        [data-testid="metric-container"] [data-testid="stMetricValue"] {
            color: #4ade80;
            font-size: 2.2rem;
            font-weight: 700;
        }

        [data-testid="metric-container"] [data-testid="stMetricLabel"] {
            color: #8b949e;
            font-size: 0.78rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.08em;
        }

        h1 { color: #e6edf3; font-weight: 700; font-size: 2rem; letter-spacing: -0.03em; }
        h2, h3 { color: #c9d1d9; font-weight: 600; }

        [data-testid="stDataFrame"] {
            border: 1px solid #30363d;
            border-radius: 8px;
        }

        [data-testid="stTabs"] [data-baseweb="tab-list"] {
            background-color: #0d1117;
            border: 1px solid #30363d;
            border-radius: 8px;
            padding: 4px;
        }

        [data-testid="stTabs"] [data-baseweb="tab"] {
            color: #8b949e;
            font-weight: 500;
            border-radius: 6px;
        }

        [data-testid="stTabs"] [aria-selected="true"] {
            background-color: #161b22;
            color: #4ade80;
        }

        [data-testid="stButton"] button {
            background: linear-gradient(135deg, #166534, #15803d);
            color: #dcfce7;
            border: 1px solid #4ade80;
            border-radius: 6px;
            font-weight: 600;
            padding: 0.5rem 1.5rem;
            transition: all 0.2s;
        }

        [data-testid="stButton"] button:hover {
            background: linear-gradient(135deg, #15803d, #16a34a);
            box-shadow: 0 0 15px rgba(74, 222, 128, 0.3);
            transform: translateY(-1px);
        }

        [data-testid="stSuccess"] {
            background-color: #052e16;
            border: 1px solid #4ade80;
            border-radius: 8px;
            color: #86efac;
        }

        [data-testid="stError"] {
            background-color: #2d0000;
            border: 1px solid #ef4444;
            border-radius: 8px;
            color: #fca5a5;
        }

        hr { border-color: #21262d; margin: 1.5rem 0; }
        </style>
        """,
        unsafe_allow_html=True,
    )
