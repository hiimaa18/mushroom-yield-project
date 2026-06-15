import json
import time
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import (
    GridSearchCV,
    TimeSeriesSplit
)
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# Start timer
start_time = time.time()

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

# Time series split
tscv = TimeSeriesSplit(
    n_splits=2
)

# Parameter grid
param_grid = {
    "n_estimators": [50, 100],
    "max_depth": [2, 3, None],
    "min_samples_leaf": [1, 2]
}

# Base model
rf = RandomForestRegressor(
    random_state=42
)

# Grid Search
grid = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    cv=tscv,
    scoring="neg_mean_absolute_error",
    n_jobs=-1
)

grid.fit(
    X_train,
    y_train
)

# Best model
best_rf = grid.best_estimator_

# Test predictions
y_pred = best_rf.predict(
    X_test
)

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

print("\nBest Parameters:")
print(grid.best_params_)

print("\nTuned RF Metrics")
print("MAE :", mae)
print("RMSE:", rmse)
print("R²  :", r2)

# Save model
joblib.dump(
    best_rf,
    "models/random_forest_tuned.joblib"
)

# Save params
with open(
    "models/rf_best_params.json",
    "w"
) as f:
    json.dump(
        grid.best_params_,
        f,
        indent=4
    )

# Save CV results
cv_results = pd.DataFrame(
    grid.cv_results_
)

cv_results.to_csv(
    "reports/gridsearch_results.csv",
    index=False
)

runtime = time.time() - start_time

print(
    f"\nRuntime: {runtime:.2f} seconds"
)