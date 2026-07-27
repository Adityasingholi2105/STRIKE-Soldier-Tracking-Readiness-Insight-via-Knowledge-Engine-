import pandas as pd
import numpy as np

# Fix randomness so we get the same "random" data every time we run this
np.random.seed(42)

# Total number of synthetic Agniveer soldiers to generate
n = 500
ids = range(1, n + 1)  # ID numbers 1 to 500

# Random age between 18-21 (realistic Agniveer entry age range)
ages = np.random.randint(18, 22, n)

# Random tenure year: which year of their 4-year contract they're in (1-4)
tenure_years = np.random.randint(1, 5, n)

# Random fitness score between 50-99
fitness_scores = np.random.randint(50, 100, n)

# Random training performance score between 40-99
training_scores = np.random.randint(40, 100, n)

# Physical test result: 1 = pass, 0 = fail
# p=[0.15, 0.85] means 15% fail, 85% pass (realistic distribution, not 50/50)
physical_test_pass = np.random.choice([0, 1], n, p=[0.15, 0.85])

# Disciplinary record: 1 = has a mark, 0 = clean
# p=[0.9, 0.1] means 90% clean record, 10% have an issue
disciplinary_record = np.random.choice([0, 1], n, p=[0.9, 0.1])

# Fitness trend over tenure: 1 = improving, 0 = declining
# p=[0.4, 0.6] means 60% improving, 40% declining
fitness_trend = np.random.choice([0, 1], n, p=[0.4, 0.6])

# Combine all factors into one score - higher score = more likely to be retained
# Fitness and training matter most (weight 0.3 each)
# Passing physical test and improving trend help; disciplinary record hurts
retention_score = (
    fitness_scores * 0.3 +
    training_scores * 0.3 +
    physical_test_pass * 20 +
    fitness_trend * 15 -
    disciplinary_record * 25
)

# Convert the raw score into a 0/1 label
# Only the TOP 25% scorers get retained (RetentionStatus = 1)
# This matches the real Agnipath retention rate (~25%)
threshold = np.percentile(retention_score, 75)
retention_status = (retention_score >= threshold).astype(int)

# Assign each soldier a random unit from this list
units = ["Para SF", "Gorkha Rifles", "Maratha Light Infantry", "Signals Corps", "Artillery Regiment"]
units_list = np.random.choice(units, n)

# Generate placeholder names since this is synthetic data
names = [f"Agniveer-{i}" for i in ids]

# Assemble all columns into one DataFrame (the final "Excel table")
df = pd.DataFrame({
    "ID": ids,
    "Name": names,
    "Age": ages,
    "Unit": units_list,
    "TenureYears": tenure_years,
    "FitnessScore": fitness_scores,
    "TrainingScore": training_scores,
    "PhysicalTestPass": physical_test_pass,
    "DisciplinaryRecord": disciplinary_record,
    "FitnessTrend": fitness_trend,
    "RetentionStatus": retention_status
})

# Save to CSV - index=False means don't add an extra row-number column
df.to_csv("agniveer_data.csv", index=False)
print(f"Generated {n} Agniveer records. Retention rate: {retention_status.mean()*100:.1f}%")