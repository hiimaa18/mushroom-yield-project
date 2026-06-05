import pandas as pd

# =========================
# LOAD CLEANED DATA
# =========================

df = pd.read_parquet("data/processed/02_cleaned.parquet")

print("Cleaned dataset loaded successfully!")

# =========================
# BASIC INFORMATION
# =========================

row_count = len(df)

date_min = df["timestamp"].min()
date_max = df["timestamp"].max()

print("\nRow Count:")
print(row_count)

print("\nDate Range:")
print(date_min, "to", date_max)

# =========================
# SUMMARY STATISTICS
# =========================

summary = df.describe().round(2)

print("\nSummary Statistics:")
print(summary)

# =========================
# VALIDITY CHECKS
# =========================

valid_humidity = ((df["humidity"] >= 0) & (df["humidity"] <= 100)).sum()

valid_co2 = (df["co2"] > 0).sum()

valid_temp = ((df["temperature"] > 0) & (df["temperature"] < 50)).sum()

total_rows = len(df)

print("\nValidity Metrics")

print(f"Humidity Valid %: {(valid_humidity/total_rows)*100:.2f}")

print(f"CO2 Valid %: {(valid_co2/total_rows)*100:.2f}")

print(f"Temperature Valid %: {(valid_temp/total_rows)*100:.2f}")

# =========================
# MEAN VS MEDIAN
# =========================

print("\nMean vs Median")

for col in ["temperature", "humidity", "co2", "yield_kg"]:

    mean = df[col].mean()
    median = df[col].median()

    print(f"{col}")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print()