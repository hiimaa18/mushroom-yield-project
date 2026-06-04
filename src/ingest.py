import pandas as pd

# =========================
# LOAD CSV
# =========================

df = pd.read_csv(
    "data/raw/polyhouse_logs.csv",
    parse_dates=["timestamp"]
)

print("Dataset Loaded Successfully!")

# =========================
# BASIC INSPECTION
# =========================

print("\nFirst 5 Rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nInfo:")
df.info()

print("\nSummary Statistics:")
print(df.describe())

# =========================
# MISSING VALUES
# =========================

print("\nMissing Values:")
print(df.isnull().sum())

# =========================
# SAVE INTERIM FILE
# =========================

df.to_csv(
    "data/interim/01_loaded.csv",
    index=False
)

print("\nInterim file saved successfully!")