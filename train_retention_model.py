import os
import pickle

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Load the agniveer dataset we generated
df = pd.read_csv("agniveer_data.csv")

# define features (inputs) and label (what we predict)
X = df[["FitnessScore", "TrainingScore", "PhysicalTestPass", "DisciplinaryRecord", "FitnessTrend", "TenureYears"]]
y = df["RetentionStatus"]

# split the data: 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# build and train the random forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# test the model and print accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# save the trained model to disk
os.makedirs("models", exist_ok=True)
with open("models/retention_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved to models/retention_model.pkl")
