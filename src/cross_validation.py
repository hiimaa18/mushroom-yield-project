import numpy as np
import pandas as pd

from sklearn.model_selection import TimeSeriesSplit
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load training data only
X = pd.read_csv(
    "data/processed/X_train.csv"
)

y = pd.read_csv(
    "data/processed/y_train.csv"
).squeeze()

# TimeSeriesSplit
tscv = TimeSeriesSplit(n_splits=3)

linear_scores = []
rf_scores = []

for train_idx, val_idx in tscv.split(X):

    X_train = X.iloc[train_idx]
    X_val = X.iloc[val_idx]

    y_train = y.iloc[train_idx]
    y_val = y.iloc[val_idx]

    # Linear Regression
    lr = LinearRegression()
    lr.fit(X_train, y_train)

    pred_lr = lr.predict(X_val)

    mae_lr = mean_absolute_error(
        y_val,
        pred_lr
    )

    linear_scores.append(mae_lr)

    # Random Forest
    rf = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    rf.fit(X_train, y_train)

    pred_rf = rf.predict(X_val)

    mae_rf = mean_absolute_error(
        y_val,
        pred_rf
    )

    rf_scores.append(mae_rf)

print("\nLinear Regression CV MAE")

for i, score in enumerate(
    linear_scores,
    start=1
):
    print(
        f"Fold {i}: {score:.4f}"
    )

print(
    "Average:",
    np.mean(linear_scores)
)

print("\nRandom Forest CV MAE")

for i, score in enumerate(
    rf_scores,
    start=1
):
    print(
        f"Fold {i}: {score:.4f}"
    )

print(
    "Average:",
    np.mean(rf_scores)
)