# Cross Validation Results

## Methodology

TimeSeriesSplit was used with 3 folds to preserve temporal ordering in the mushroom yield dataset.

Unlike random K-Fold validation, TimeSeriesSplit ensures that future observations are never used to predict past observations.

Only the training dataset was used during cross-validation. The held-out test dataset remained untouched.

---

## Cross-Validated MAE

| Model             | Fold 1 | Fold 2 | Fold 3 | Average MAE |
| ----------------- | ------ | ------ | ------ | ----------- |
| Linear Regression | 0.3000 | 0.3054 | 0.1771 | 0.2608      |
| Random Forest     | 0.3000 | 0.4660 | 0.0720 | 0.2793      |

---

## Comparison with Hold-Out Test Results

| Model             | CV MAE | Test MAE |
| ----------------- | ------ | -------- |
| Linear Regression | 0.2608 | 0.2560   |
| Random Forest     | 0.2793 | 0.3850   |

---

## Overfitting Analysis

Linear Regression:

* CV MAE = 0.2608
* Test MAE = 0.2560

The cross-validation and test errors are very similar, suggesting stable performance and little evidence of overfitting.

Random Forest:

* CV MAE = 0.2793
* Test MAE = 0.3850

The test error is noticeably larger than the average cross-validation error. This may indicate mild overfitting or instability due to the very small dataset size.

---

## Variance Across Folds

Linear Regression showed relatively consistent performance across folds.

Random Forest showed larger variation between folds, ranging from 0.0720 to 0.4660 MAE.

This suggests that Random Forest performance is more sensitive to changes in the training data and may require additional observations before reliable tuning can be performed.

---

## Interpretation

The results indicate that Linear Regression remains the more stable and reliable model for the current dataset.

Although Random Forest can model nonlinear relationships, the available data volume is too small to consistently benefit from the additional complexity.

Future work should focus on collecting more observations and performing systematic hyperparameter tuning using GridSearch before making final model selections.
