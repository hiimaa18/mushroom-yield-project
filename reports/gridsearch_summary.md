# GridSearchCV Tuning Summary

## Parameter Grid

The following Random Forest hyperparameters were tuned:

* n_estimators = [50, 100]
* max_depth = [2, 3, None]
* min_samples_leaf = [1, 2]

### Rationale

* n_estimators controls the number of trees in the forest.
* max_depth controls tree complexity and helps prevent overfitting.
* min_samples_leaf specifies the minimum number of samples required in a leaf node.

---

## Validation Strategy

GridSearchCV was performed using TimeSeriesSplit cross-validation.

This approach preserves temporal ordering and prevents future observations from influencing past predictions.

Only training data was used during tuning.

---

## Best Parameters

```json
{
  "max_depth": 2,
  "min_samples_leaf": 1,
  "n_estimators": 50
}
```

---

## Tuned Model Evaluation

| Metric | Value  |
| ------ | ------ |
| MAE    | 0.3920 |
| RMSE   | 0.3920 |
| R²     | 0.4920 |

---

## Runtime

GridSearchCV completed in approximately 4.66 seconds.

The search space was intentionally small to keep execution time reasonable on a standard laptop.

---

## Conclusion

GridSearchCV successfully identified the best-performing Random Forest configuration within the defined parameter grid.

However, the tuned Random Forest model did not outperform either the default Random Forest model or the Linear Regression baseline.

Given the limited dataset size, Linear Regression remains the preferred model for this project due to its superior predictive performance and simplicity.
