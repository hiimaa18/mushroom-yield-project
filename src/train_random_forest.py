import os
import json
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# Load data
X_train = pd.read_csv(
    "data/processed/X_train.csv"
)

X_test = pd.read_csv(
    "data/processed/X_test.csv"
)

y_train = pd.read_csv(
    "data/processed/y_train.csv"
).squeeze()

y_test = pd.read_csv(
    "data/processed/y_test.csv"
).squeeze()

# Train model
rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

rf.fit(
    X_train,
    y_train
)

# Predict
y_pred = rf.predict(X_test)

# Metrics
mae = mean_absolute_error(
    y_test,
    y_pred
)

rmse = mean_squared_error(
    y_test,
    y_pred
) ** 0.5

r2 = r2_score(
    y_test,
    y_pred
)

print("\nRandom Forest Metrics")
print("MAE :", mae)
print("RMSE:", rmse)
print("R²  :", r2)

# Save metrics
metrics = {
    "MAE": float(mae),
    "RMSE": float(rmse),
    "R2": float(r2)
}

os.makedirs(
    "reports",
    exist_ok=True
)

with open(
    "reports/random_forest_metrics.json",
    "w"
) as f:
    json.dump(
        metrics,
        f,
        indent=4
    )

# Save model
joblib.dump(
    rf,
    "models/random_forest.joblib"
)

# Feature importance plot
importance = rf.feature_importances_

plt.figure(figsize=(6,4))

plt.bar(
    X_train.columns,
    importance
)

plt.title(
    "Random Forest Feature Importance"
)

plt.ylabel(
    "Importance"
)

plt.tight_layout()

plt.savefig(
    "reports/figures/rf_feature_importance.png"
)

plt.close()

print(
    "\nModel and feature importance saved."
)