import os
import pandas as pd

def load_data(csv_path):
    """Load data from a CSV file and handle errors."""
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV file not found at {csv_path}")
    return pd.read_csv(csv_path)

def calculate_metrics(df):
    """Calculate readiness and risk metrics."""
    def advanced_readiness_score(row):
        return round((0.5 * row['FitnessScore']) + (0.3 * row['YearsOfService']) - (0.2 * row['Age']), 2)

    def readiness_status(score):
        if score >= 75:
            return 'Fit'
        elif score >= 60:
            return 'Watchlist'
        return 'Unfit'

    def risk_score(row):
        return round(100 - row['FitnessScore'] + (row['Age'] / 2) - row['YearsOfService'])

    def risk_category(score):
        if score > 50:
            return 'High'
        elif score > 30:
            return 'Medium'
        return 'Low'

    df['ReadinessScore'] = df.apply(advanced_readiness_score, axis=1)
    df['ReadinessStatus'] = df['ReadinessScore'].apply(readiness_status)
    df['RiskScore'] = df.apply(risk_score, axis=1)
    df['RiskCategory'] = df['RiskScore'].apply(risk_category)
    return df
