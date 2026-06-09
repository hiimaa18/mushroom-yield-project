"""
Features:

temperature:
    Air temperature in Celsius.

humidity:
    Relative humidity percentage.

co2:
    Carbon dioxide concentration in ppm.

temp_humidity:
    temperature × humidity interaction feature.

Target:

yield_kg:
    Mushroom yield in kilograms.
"""

import os
import pandas as pd
import joblib
from sklearn.preprocessing import MinMaxScaler

# Load cleaned data
df = pd.read_csv("sample_cleaned_data.csv")

# Create engineered feature
df["temp_humidity"] = df["temperature"] * df["humidity"]

# Define features and target
X = df[
    [
        "temperature",
        "humidity",
        "co2",
        "temp_humidity"
    ]
]

y = df["yield_kg"]

# Check for missing values
print("\nMissing values in X:")
print(X.isna().sum())

print("\nMissing values in y:")
print(y.isna().sum())

# Scale features
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Convert back to DataFrame
X_scaled = pd.DataFrame(
    X_scaled,
    columns=X.columns
)

# Check ranges
print("\nMinimum values:")
print(X_scaled.min())

print("\nMaximum values:")
print(X_scaled.max())

# Check shapes
print("\nShapes:")
print("X shape:", X_scaled.shape)
print("y shape:", y.shape)

# Create folders if they don't exist
os.makedirs("models", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

# Save scaler
joblib.dump(
    scaler,
    "models/minmax_scaler.pkl"
)

# Save processed features
X_scaled.to_parquet(
    "data/processed/features.parquet",
    index=False
)

print("\nFiles saved successfully!")
print("models/minmax_scaler.pkl")
print("data/processed/features.parquet")