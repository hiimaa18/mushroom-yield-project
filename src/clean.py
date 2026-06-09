import pandas as pd

# =========================
# LOAD DATA
# =========================

df = pd.read_csv("data/raw/polyhouse_logs.csv")

print("Dataset Loaded Successfully")
print(df.head())

# =========================
# BASIC INFO
# =========================

print("\nShape of dataset:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

# =========================
# MISSING VALUE REPORT
# =========================

print("\nMissing Values Report")

missing_count = df.isnull().sum()
missing_percent = (df.isnull().sum() / len(df)) * 100

missing_report = pd.DataFrame({
    "Missing Count": missing_count,
    "Missing %": missing_percent
})

print(missing_report)

# =========================
# HANDLE MISSING VALUES
# =========================

# Forward fill sensor columns
sensor_columns = ["temperature", "humidity", "co2"]

for col in sensor_columns:
    df[col] = df[col].ffill()

# Remove rows where target is missing
df = df.dropna(subset=["yield_kg"])

# Fill remaining numeric nulls with median
numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# =========================
# REMOVE DUPLICATES
# =========================

before_duplicates = len(df)

df = df.drop_duplicates()

after_duplicates = len(df)

print("\nDuplicates Removed:")
print(before_duplicates - after_duplicates)

# =========================
# VALIDITY RULES
# =========================

# Humidity should be between 0 and 100
df = df[(df["humidity"] >= 0) & (df["humidity"] <= 100)]

# CO2 should be positive
df = df[df["co2"] > 0]

# Temperature basic validity
df = df[(df["temperature"] > 0) & (df["temperature"] < 50)]

# =========================
# OUTLIER CHECK
# =========================

print("\nPotential Outliers")

for col in ["temperature", "humidity", "co2", "yield_kg"]:

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[(df[col] < lower) | (df[col] > upper)]

    print(f"{col}: {len(outliers)} outliers")

# =========================
# FINAL CHECK
# =========================

print("\nFinal Missing Values")
print(df.isnull().sum())

print("\nFinal Shape")
print(df.shape)

# =========================
# SAVE CLEANED DATA
# =========================

df.to_parquet("data/processed/02_cleaned.parquet", index=False)

print("\nCleaned dataset saved successfully!")