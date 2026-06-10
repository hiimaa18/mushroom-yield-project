import os
import json
import joblib
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# Load Day 8 outputs
X_train = pd.read_csv(
    "data/processed/X_train.csv"
)

X_test = pd.read_csv(
    "data/processed/X_test.csv"
)

y_train = pd.read_csv(
    "data/processed/y_train.csv"
)

y_test = pd.read_csv(
    "data/processed/y_test.csv"
)

# Convert target to series
y_train = y_train.squeeze()
y_test = y_test.squeeze()

# Train model
model = LinearRegression()

model.fit(
    X_train,
    y_train
)

# Predictions
train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

# Metrics
mae = mean_absolute_error(
    y_test,
    test_pred
)

rmse = mean_squared_error(
    y_test,
    test_pred
) ** 0.5

r2 = r2_score(
    y_test,
    test_pred
)

# Print metrics
print("\nTest Metrics")
print("MAE :", mae)
print("RMSE:", rmse)
print("R²  :", r2)

# Coefficients
print("\nCoefficients")

for feature, coef in zip(
    X_train.columns,
    model.coef_
):
    print(
        f"{feature}: {coef:.4f}"
    )

# Create folders
os.makedirs(
    "reports",
    exist_ok=True
)

os.makedirs(
    "models",
    exist_ok=True
)

# Save metrics
metrics = {
    "MAE": float(mae),
    "RMSE": float(rmse),
    "R2": float(r2)
}

with open(
    "reports/metrics_linear.json",
    "w"
) as f:
    json.dump(
        metrics,
        f,
        indent=4
    )

# Save model
joblib.dump(
    model,
    "models/linear_regression.joblib"
)

print(
    "\nSaved model and metrics."
)