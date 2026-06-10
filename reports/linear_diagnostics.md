# Linear Regression Diagnostics

## Residual Definition

Residuals were calculated as:

Residual = Actual Yield − Predicted Yield

Positive residuals indicate under-prediction by the model.

Negative residuals indicate over-prediction.

---

## Diagnostic Plots

1. residuals_linear.png
2. residuals_vs_humidity_linear.png

---

## Findings

The residual plots were reviewed to determine whether prediction errors appeared random or showed visible structure.

Due to the very small dataset size (6 observations), diagnostic conclusions are limited.

No strong conclusion regarding heteroscedasticity can be made because the test set contains only two observations.

Residual patterns should be re-evaluated after collecting additional sensor records.

---

## Modeling Recommendation

Linear regression provides an interpretable baseline and achieved a positive R² score.

However, mushroom growth may involve nonlinear relationships between environmental variables.

Future experimentation with Random Forest models is recommended to evaluate whether nonlinear interactions improve predictive performance.

The linear model should be retained as a baseline for future comparisons.
