import numpy as np
from sklearn.linear_model import LinearRegression
import joblib
import os

# Create dummy data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Train model
model = LinearRegression()
model.fit(X, y)

# Ensure model directory exists
os.makedirs("model", exist_ok=True)

# Save model
joblib.dump(model, "model/regression_model.pkl")

print("✅ Model trained and saved at model/regression_model.pkl")
