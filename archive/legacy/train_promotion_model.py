import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# Load the dataset
csv_path = "strike_data.csv"
df = pd.read_csv(csv_path)

# Prepare the data for training
X = df[['FitnessScore', 'YearsOfService', 'Age']]
y = df['PromotionEligible']  # Ensure this column exists in your dataset

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save the model
model_path = "models/promotion_model.pkl"
with open(model_path, 'wb') as file:
    pickle.dump(model, file)
print(f"Model saved to {model_path}")
