import os
import pandas as pd
import joblib

from sklearn.preprocessing import MinMaxScaler

# Load dataset
df = pd.read_csv("sample_cleaned_data.csv")

# Convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Sort chronologically
df = df.sort_values("timestamp")

# Create feature
df["temp_humidity"] = (
    df["temperature"] *
    df["humidity"]
)

# Features
X = df[
    [
        "temperature",
        "humidity",
        "co2",
        "temp_humidity"
    ]
]

# Target
y = df["yield_kg"]

# 80/20 chronological split
split_index = int(len(df) * 0.8)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

# Dates
train_start = df.iloc[0]["timestamp"]
train_end = df.iloc[split_index - 1]["timestamp"]

test_start = df.iloc[split_index]["timestamp"]
test_end = df.iloc[-1]["timestamp"]

print("\nTrain Period:")
print(train_start, "to", train_end)

print("\nTest Period:")
print(test_start, "to", test_end)

# Fit scaler ONLY on train
scaler = MinMaxScaler()

X_train_scaled = scaler.fit_transform(X_train)

# Transform test
X_test_scaled = scaler.transform(X_test)

# Back to DataFrames
X_train_scaled = pd.DataFrame(
    X_train_scaled,
    columns=X.columns
)

X_test_scaled = pd.DataFrame(
    X_test_scaled,
    columns=X.columns
)

# Save folders
os.makedirs(
    "data/processed",
    exist_ok=True
)

os.makedirs(
    "models",
    exist_ok=True
)

# Save splits
X_train_scaled.to_csv(
    "data/processed/X_train.csv",
    index=False
)

X_test_scaled.to_csv(
    "data/processed/X_test.csv",
    index=False
)

y_train.to_csv(
    "data/processed/y_train.csv",
    index=False
)

y_test.to_csv(
    "data/processed/y_test.csv",
    index=False
)

# Save scaler
joblib.dump(
    scaler,
    "models/minmax_scaler.pkl"
)

print("\nTrain Size:", len(X_train))
print("Test Size:", len(X_test))

print("\nFiles Saved Successfully!")