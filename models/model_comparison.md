# Model Comparison

| Model             | MAE   | RMSE  | R²    |
| ----------------- | ----- | ----- | ----- |
| Linear Regression | 0.256 | 0.349 | 0.598 |
| Random Forest     | 0.385 | 0.385 | 0.511 |

## Analysis

Linear Regression outperformed Random Forest on all evaluation metrics.

The Linear Regression model achieved:

* Lower MAE
* Lower RMSE
* Higher R²

This indicates that Linear Regression provided more accurate predictions on the available test dataset.

## Complexity Assessment

Random Forest is capable of modeling nonlinear relationships and feature interactions. However, in this project it did not improve predictive performance compared to the simpler Linear Regression model.

Because the dataset contains only a small number of observations, Random Forest may not have enough data to fully benefit from its additional complexity.

## Recommendation

Linear Regression should remain the preferred baseline model for this dataset.

Random Forest does not currently justify its added complexity because it produced lower predictive performance on the test set.

Future experiments with larger datasets and hyperparameter tuning may improve Random Forest performance.
