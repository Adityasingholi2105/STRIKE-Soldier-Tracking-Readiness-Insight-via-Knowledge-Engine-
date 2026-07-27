import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from typing import Optional
import os
from datetime import datetime

# CONFIGURATION
CSV_FILE = 'personnel_data.csv'  # Update this path as needed
EXPORT_FOLDER = 'reports'  # Folder for exported reports

# DATA LOADING
def load_personnel_data(csv_path):
    """Load personnel data from a CSV file into a pandas DataFrame."""
    try:
        df = pd.read_csv(csv_path)
        print(f"Loaded {len(df)} records from {csv_path}.")
        return df
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None

# BASIC ANALYTICS FUNCTIONS
def show_total_personnel(df):
    """Display total personnel count."""
    print(f"Total personnel: {len(df)}")

def show_average_age_and_fitness(df):
    """Display average age and average fitness score."""
    avg_age = df['Age'].mean()
    avg_fitness = df['FitnessScore'].mean()
    print(f"Average Age: {avg_age:.2f}")
    print(f"Average Fitness Score: {avg_fitness:.2f}")

def show_top_ranks(df, top_n=3):
    """Display the top N most common ranks."""
    top_ranks = df['Rank'].value_counts().head(top_n)
    print(f"Top {top_n} Ranks:")
    print(top_ranks)

def plot_rank_distribution(df):
    """Plot a bar chart of rank distribution."""
    rank_counts = df['Rank'].value_counts()
    rank_counts.plot(kind='bar', title='Rank Distribution')
    plt.xlabel('Rank')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()

def plot_unit_distribution(df):
    """Plot a pie chart of unit distribution."""
    unit_counts = df['Unit'].value_counts()
    unit_counts.plot(kind='pie', autopct='%1.1f%%', title='Unit Distribution')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()

def show_low_fitness(df, threshold=70):
    """Display all soldiers with FitnessScore below the threshold."""
    low_fit = df[df['FitnessScore'] < threshold]
    print(f"Soldiers with FitnessScore < {threshold}:")
    print(low_fit[['ID', 'Name', 'FitnessScore', 'Unit', 'Rank']])

# ADVANCED ANALYTICS FUNCTIONS
def calculate_readiness_status(df):
    """
    Calculate readiness status based on fitness and age criteria.
    Returns DataFrame with new ReadinessStatus column.
    """
    conditions = [
        (df['FitnessScore'] > 75) & (df['Age'] < 35),
        ((df['FitnessScore'].between(60, 75)) | (df['Age'] > 40))
    ]
    choices = ['Fit', 'Watchlist']
    df['ReadinessStatus'] = np.select(conditions, choices, default='Unfit')
    return df

def analyze_unit_fitness(df):
    """
    Group by Unit and show average FitnessScore.
    Returns sorted DataFrame of unit-wise fitness metrics.
    """
    unit_fitness = df.groupby('Unit').agg({
        'FitnessScore': ['mean', 'min', 'max', 'count']
    }).round(2)
    unit_fitness.columns = ['Avg_Fitness', 'Min_Fitness', 'Max_Fitness', 'Personnel_Count']
    return unit_fitness.sort_values('Avg_Fitness', ascending=False)

def calculate_promotion_eligibility(df):
    """
    Calculate promotion eligibility based on fitness and years of service.
    Returns DataFrame with new PromotionEligible column.
    """
    df['PromotionEligible'] = (
        (df['FitnessScore'] > 80) & 
        (df['YearsOfService'] > 5)
    ).map({True: 'Yes', False: 'No'})
    return df

def calculate_risk_score(df):
    """
    Calculate risk score and category based on multiple factors.
    Returns DataFrame with new RiskScore and RiskCategory columns.
    """
    df['RiskScore'] = (
        100 - df['FitnessScore'] + 
        (df['Age'] / 2) - 
        df['YearsOfService']
    ).round(2)
    
    conditions = [
        df['RiskScore'] >= 50,
        df['RiskScore'].between(30, 49.99)
    ]
    choices = ['High', 'Medium']
    df['RiskCategory'] = np.select(conditions, choices, default='Low')
    return df

def filter_personnel(df, filter_type: str, filter_value: Optional[str] = None):
    """
    Filter personnel data based on user input.
    Args:
        df: DataFrame containing personnel data
        filter_type: Type of filter ('unit' or 'rank')
        filter_value: Value to filter by (optional)
    """
    if filter_value is None:
        if filter_type.lower() == 'unit':
            print("\nAvailable Units:")
            print(df['Unit'].unique())
            filter_value = input("\nEnter Unit name to filter: ")
        elif filter_type.lower() == 'rank':
            print("\nAvailable Ranks:")
            print(df['Rank'].unique())
            filter_value = input("\nEnter Rank to filter: ")
    
    if filter_type.lower() == 'unit':
        return df[df['Unit'].str.contains(filter_value, case=False)]
    elif filter_type.lower() == 'rank':
        return df[df['Rank'].str.contains(filter_value, case=False)]
    else:
        print("Invalid filter type. Use 'unit' or 'rank'.")
        return df

def export_data(df, filename: str):
    """Export DataFrame to CSV in the reports folder."""
    if not os.path.exists(EXPORT_FOLDER):
        os.makedirs(EXPORT_FOLDER)
    
    filepath = os.path.join(EXPORT_FOLDER, filename)
    df.to_csv(filepath, index=False)
    print(f"Data exported to {filepath}")

def export_risk_analysis(df, filename: str):
    """
    Export detailed risk analysis report in both CSV and text formats.
    Includes summary statistics, detailed breakdowns, and recommendations.
    """
    if not os.path.exists(EXPORT_FOLDER):
        os.makedirs(EXPORT_FOLDER)
    
    # Calculate risk analysis if not already done
    if 'RiskScore' not in df.columns:
        df = calculate_risk_score(df)
    
    # Create report filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    base_filename = os.path.splitext(filename)[0]
    csv_path = os.path.join(EXPORT_FOLDER, f"{base_filename}_{timestamp}.csv")
    txt_path = os.path.join(EXPORT_FOLDER, f"{base_filename}_{timestamp}.txt")
    
    # Export full data to CSV
    df.to_csv(csv_path, index=False)
    
    # Generate detailed text report
    with open(txt_path, 'w') as f:
        # Header
        f.write("=== STRIKE FORCE RISK ANALYSIS REPORT ===\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        # Overall Statistics
        f.write("1. OVERALL RISK DISTRIBUTION\n")
        f.write("-" * 30 + "\n")
        risk_dist = df['RiskCategory'].value_counts()
        for category, count in risk_dist.items():
            percentage = (count / len(df)) * 100
            f.write(f"{category} Risk: {count} personnel ({percentage:.1f}%)\n")
        f.write("\n")
        
        # Unit-wise Risk Analysis
        f.write("2. UNIT-WISE RISK ANALYSIS\n")
        f.write("-" * 30 + "\n")
        unit_risk = df.groupby('Unit')['RiskCategory'].value_counts().unstack(fill_value=0)
        for unit in unit_risk.index:
            f.write(f"\n{unit}:\n")
            for category in ['High', 'Medium', 'Low']:
                if category in unit_risk.columns:
                    count = unit_risk.loc[unit, category]
                    f.write(f"  - {category} Risk: {count}\n")
        f.write("\n")
        
        # High Risk Personnel Details
        f.write("3. HIGH RISK PERSONNEL DETAILS\n")
        f.write("-" * 30 + "\n")
        high_risk = df[df['RiskCategory'] == 'High'].sort_values('RiskScore', ascending=False)
        for _, person in high_risk.iterrows():
            f.write(f"\nName: {person['Name']}\n")
            f.write(f"Unit: {person['Unit']}\n")
            f.write(f"Rank: {person['Rank']}\n")
            f.write(f"Age: {person['Age']}\n")
            f.write(f"Fitness Score: {person['FitnessScore']}\n")
            f.write(f"Risk Score: {person['RiskScore']:.1f}\n")
            
            # Generate personalized recommendations
            f.write("Recommendations:\n")
            if person['FitnessScore'] < 60:
                f.write("- Immediate fitness improvement program required\n")
            if person['Age'] > 45:
                f.write("- Consider age-appropriate training modifications\n")
            if person['YearsOfService'] < 5:
                f.write("- Additional training and mentoring recommended\n")
        f.write("\n")
        
        # Summary and Recommendations
        f.write("4. GENERAL RECOMMENDATIONS\n")
        f.write("-" * 30 + "\n")
        f.write("1. Implement regular fitness assessments for high-risk personnel\n")
        f.write("2. Develop targeted training programs for different risk categories\n")
        f.write("3. Consider unit-specific risk mitigation strategies\n")
        f.write("4. Regular monitoring of personnel with Risk Scores above 50\n")
        f.write("5. Establish mentoring programs pairing low-risk with high-risk personnel\n")
    
    print(f"\nDetailed risk analysis exported to:")
    print(f"1. CSV data: {csv_path}")
    print(f"2. Text report: {txt_path}")

# MAIN EXECUTION
def main():
    # Load data
    df = load_personnel_data(CSV_FILE)
    if df is None:
        return

    while True:
        print("\n=== Military Personnel Analytics System ===")
        print("1. Basic Analytics")
        print("2. Readiness Analysis")
        print("3. Unit-wise Fitness Analysis")
        print("4. Promotion Eligibility Analysis")
        print("5. Filter Personnel")
        print("6. Risk Analysis")
        print("7. Export Risk Analysis Report")
        print("8. Exit")
        
        choice = input("\nEnter your choice (1-8): ")
        
        if choice == '1':
            show_total_personnel(df)
            show_average_age_and_fitness(df)
            show_top_ranks(df)
            plot_rank_distribution(df)
            plot_unit_distribution(df)
            show_low_fitness(df)
        
        elif choice == '2':
            df = calculate_readiness_status(df)
            readiness_counts = df['ReadinessStatus'].value_counts()
            print("\nReadiness Status Distribution:")
            print(readiness_counts)
            print("\nPersonnel on Watchlist or Unfit:")
            print(df[df['ReadinessStatus'] != 'Fit'][['Name', 'Age', 'FitnessScore', 'ReadinessStatus']])
        
        elif choice == '3':
            unit_fitness = analyze_unit_fitness(df)
            print("\nUnit-wise Fitness Analysis:")
            print(unit_fitness)
        
        elif choice == '4':
            df = calculate_promotion_eligibility(df)
            eligible_count = (df['PromotionEligible'] == 'Yes').sum()
            print(f"\nTotal Eligible for Promotion: {eligible_count}")
            print("\nEligible Personnel:")
            print(df[df['PromotionEligible'] == 'Yes'][['Name', 'Rank', 'FitnessScore', 'YearsOfService']])
        
        elif choice == '5':
            filter_type = input("Enter filter type (unit/rank): ").lower()
            filtered_df = filter_personnel(df, filter_type)
            print("\nFiltered Personnel:")
            print(filtered_df[['Name', 'Rank', 'Unit', 'FitnessScore']])
        
        elif choice == '6':
            df = calculate_risk_score(df)
            risk_counts = df['RiskCategory'].value_counts()
            print("\nRisk Category Distribution:")
            print(risk_counts)
            print("\nHigh Risk Personnel:")
            print(df[df['RiskCategory'] == 'High'][['Name', 'Age', 'FitnessScore', 'RiskScore', 'RiskCategory']])
        
        elif choice == '7':
            filename = input("Enter report name (without extension): ")
            if not filename:
                filename = 'risk_analysis'
            export_risk_analysis(df, filename)
        
        elif choice == '8':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()