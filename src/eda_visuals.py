import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# LOAD CLEANED DATA
# =========================

df = pd.read_parquet(
    "data/processed/02_cleaned.parquet"
)

print("Dataset Loaded Successfully!")

# =========================
# CREATE FIGURES FOLDER
# =========================

# Correlation uses only numeric columns
numeric_df = df.select_dtypes(include=["float64", "int64"])

# =========================
# CORRELATION HEATMAP
# =========================

plt.figure(figsize=(8, 6))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig(
    "reports/figures/correlation_heatmap.png"
)

plt.close()

# =========================
# HUMIDITY VS YIELD
# =========================

plt.figure(figsize=(6, 5))

plt.scatter(
    df["humidity"],
    df["yield_kg"],
    alpha=0.7
)

plt.xlabel("Humidity (%)")
plt.ylabel("Yield (kg)")
plt.title("Humidity vs Yield")

plt.tight_layout()

plt.savefig(
    "reports/figures/humidity_vs_yield.png"
)

plt.close()

# =========================
# TEMPERATURE VS YIELD
# =========================

plt.figure(figsize=(6, 5))

plt.scatter(
    df["temperature"],
    df["yield_kg"],
    alpha=0.7
)

plt.xlabel("Temperature (°C)")
plt.ylabel("Yield (kg)")
plt.title("Temperature vs Yield")

plt.tight_layout()

plt.savefig(
    "reports/figures/temperature_vs_yield.png"
)

plt.close()

# =========================
# CO2 VS YIELD
# =========================

plt.figure(figsize=(6, 5))

plt.scatter(
    df["co2"],
    df["yield_kg"],
    alpha=0.7
)

plt.xlabel("CO₂ (ppm)")
plt.ylabel("Yield (kg)")
plt.title("CO₂ vs Yield")

plt.tight_layout()

plt.savefig(
    "reports/figures/co2_vs_yield.png"
)

plt.close()

print("EDA figures saved successfully!")