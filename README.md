# STRIKE

STRIKE is a soldier tracking and readiness insight dashboard built with Streamlit. It helps command teams review personnel data, analyze readiness metrics, and explore retention and promotion prediction workflows.

## Features

- Personnel overview dashboard
- Readiness analytics visualizations
- Retention predictor interface
- Export tools for report generation
- Machine learning workflows for prediction modeling

## Project Structure

- `strike_dashboard.py` — main Streamlit app entry point
- `pages/` — dashboard pages for overview, analytics, and retention prediction
- `utils/` — reusable helper modules
- `train_*.py` — training scripts for predictive models
- `models/` — serialized machine learning models

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the dashboard:
   ```bash
   streamlit run strike_dashboard.py
   ```

## Requirements

- Python 3.10+
- Streamlit
- Pandas
- Plotly
- scikit-learn
- openpyxl
