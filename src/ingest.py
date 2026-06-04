import pandas as pd

# Load CSV
df = pd.read_csv(
    "data/raw/polyhouse_sensors.csv",
    parse_dates=["timestamp"]
)

# Print details
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nInfo:")
print(df.info())

print("\nSummary:")
print(df.describe())

# Save interim file
df.to_csv(
    "data/interim/01_loaded.csv",
    index=False
)

print("\nFile saved successfully!")