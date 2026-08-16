# STRIKE

STRIKE is a defense analytics dashboard built with Streamlit for monitoring soldier readiness, tracking personnel data, and predicting retention risk. It provides commanders with a concise operational view of workforce performance and helps identify personnel who may need support, training, or intervention.

## Features

- Personnel overview dashboard
- Readiness analytics and unit fitness monitoring
- Retention prediction workflows using ML
- Data-driven operational insights for workforce planning
- Clean, dark-themed UI designed for command dashboards

## Project Structure

- `strike_dashboard.py` — main Streamlit entry point
- `pages/` — overview, readiness, and retention pages
- `utils/` — shared styling and helper utilities
- `models/` — trained model artifacts
- `agniveer_data.csv` — main dataset used by the dashboard
- `train_retention_model.py` — script to retrain the retention model
- `generate_agniveer_data.py` — synthetic data generator

## Setup

1. Clone the repository
2. Create a virtual environment if needed
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   streamlit run strike_dashboard.py
   ```

## Requirements

- Python 3.10+
- Streamlit
- Pandas
- NumPy
- Plotly
- scikit-learn
- Matplotlib
- openpyxl
