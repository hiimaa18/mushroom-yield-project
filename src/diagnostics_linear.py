import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt

# Load data
X_test = pd.read_csv(
    "data/processed/X_test.csv"
)

y_test = pd.read_csv(
    "data/processed/y_test.csv"
).squeeze()

# Load model
model = joblib.load(
    "models/linear_regression.joblib"
)

# Predict
y_pred = model.predict(X_test)

# Residuals
residuals = y_test - y_pred

# Create folder
os.makedirs(
    "reports/figures",
    exist_ok=True
)

# Plot 1
plt.figure(figsize=(6,4))
plt.scatter(y_pred, residuals)

plt.axhline(
    0,
    linestyle="--"
)

plt.xlabel(
    "Predicted Yield"
)

plt.ylabel(
    "Residuals"
)

plt.title(
    "Residuals vs Predicted Yield"
)

plt.tight_layout()

plt.savefig(
    "reports/figures/residuals_linear.png"
)

plt.close()

# Plot 2
plt.figure(figsize=(6,4))

plt.scatter(
    X_test["humidity"],
    residuals
)

plt.axhline(
    0,
    linestyle="--"
)

plt.xlabel(
    "Humidity"
)

plt.ylabel(
    "Residuals"
)

plt.title(
    "Residuals vs Humidity"
)

plt.tight_layout()

plt.savefig(
    "reports/figures/residuals_vs_humidity_linear.png"
)

plt.close()

print("Diagnostic plots saved.")