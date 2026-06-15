import pandas as pd
import joblib
import matplotlib.pyplot as plt
import os

# Load test data
X_test = pd.read_csv("data/processed/X_test.csv")

y_test = pd.read_csv(
    "data/processed/y_test.csv"
).squeeze()

# Load champion model
model = joblib.load(
    "models/linear_regression.joblib"
)

# Predict
y_pred = model.predict(X_test)

os.makedirs(
    "reports/figures",
    exist_ok=True
)

# Plot
plt.figure(figsize=(6,4))

plt.scatter(
    y_test,
    y_pred
)

plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()]
)

plt.xlabel("Actual Yield")
plt.ylabel("Predicted Yield")
plt.title("Predicted vs Actual Yield")

plt.tight_layout()

plt.savefig(
    "reports/figures/pred_vs_actual_linear.png"
)

plt.show()