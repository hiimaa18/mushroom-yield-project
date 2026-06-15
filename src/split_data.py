import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib

# Load dataset
df = pd.read_parquet(
    "data/processed/02_cleaned.parquet"
)

print(df.columns)

# Convert timestamp
df["timestamp"] = pd.to_datetime(
    df["timestamp"]
)

# Sort chronologically
df = df.sort_values("timestamp")

print(df["timestamp"].head())
print(df["timestamp"].tail())

# 80/20 split
split_idx = int(len(df) * 0.8)

train_df = df.iloc[:split_idx].copy()
test_df = df.iloc[split_idx:].copy()

print("Train size:", len(train_df))
print("Test size:", len(test_df))

print("Train starts:",
      train_df["timestamp"].min())

print("Train ends:",
      train_df["timestamp"].max())

print("Test starts:",
      test_df["timestamp"].min())

print("Test ends:",
      test_df["timestamp"].max())

assert (
    train_df["timestamp"].max()
    <
    test_df["timestamp"].min()
)

# Feature engineering
train_df["temp_humidity_interaction"] = (
    train_df["temperature"] *
    train_df["humidity"]
)

test_df["temp_humidity_interaction"] = (
    test_df["temperature"] *
    test_df["humidity"]
)

# Features
features = [
    "temperature",
    "humidity",
    "co2",
    "temp_humidity_interaction"
]

X_train = train_df[features]
X_test = test_df[features]

# Target
y_train = train_df["yield_kg"]
y_test = test_df["yield_kg"]

# Scaling
scaler = MinMaxScaler()

X_train_scaled = scaler.fit_transform(
    X_train
)

X_test_scaled = scaler.transform(
    X_test
)

# Convert back to DataFrames
X_train_scaled = pd.DataFrame(
    X_train_scaled,
    columns=features
)

X_test_scaled = pd.DataFrame(
    X_test_scaled,
    columns=features
)

# Save processed files
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

# Save train/test datasets
train_df.to_csv(
    "data/processed/train.csv",
    index=False
)

test_df.to_csv(
    "data/processed/test.csv",
    index=False
)

# Save scaler
joblib.dump(
    scaler,
    "data/processed/minmax_scaler.pkl"
)

print("\nChronological split complete")
print("Train CSV saved")
print("Test CSV saved")
print("Scaler saved")