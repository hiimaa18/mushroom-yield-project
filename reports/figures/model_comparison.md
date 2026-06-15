# Model Comparison Report

## Objective

Compare the performance of Linear Regression, Default Random Forest, and Tuned Random Forest models for mushroom yield prediction.

---

## Performance Summary

| Model                   | MAE    | RMSE   | R²     |
| ----------------------- | ------ | ------ | ------ |
| Linear Regression       | 0.2560 | 0.3490 | 0.5980 |
| Random Forest (Default) | 0.3845 | 0.3845 | 0.5112 |
| Random Forest (Tuned)   | 0.0031 | 0.0053 | 0.9999 |

---

## Cross-Validation Results

| Model                   | Fold 1 MAE | Fold 2 MAE | Fold 3 MAE | Average CV MAE |
| ----------------------- | ---------- | ---------- | ---------- | -------------- |
| Linear Regression       | 0.3000     | 0.3054     | 0.1771     | 0.2608         |
| Random Forest (Default) | 0.3000     | 0.4660     | 0.0720     | 0.2793         |

---

## GridSearchCV Results

Best Parameters:

```text
{
    'max_depth': None,
    'min_samples_leaf': 1,
    'n_estimators': 50
}
```

Tuned Random Forest Metrics:

```text
MAE  : 0.0031
RMSE : 0.0053
R²   : 0.9999
```

Runtime:

```text
6.13 seconds
```

---

## Champion Model Selection

Champion Model: Tuned Random Forest

Reasons:

1. Lowest Mean Absolute Error (MAE)
2. Lowest Root Mean Squared Error (RMSE)
3. Highest R² Score
4. Best overall predictive performance

Champion Model File:

```text
models/champion.joblib
```

---

## Conclusion

Linear Regression initially provided a strong baseline and outperformed the default Random Forest model.

After hyperparameter tuning using GridSearchCV, the Tuned Random Forest achieved substantially better performance, producing near-perfect predictions on the test dataset.

Therefore, the Tuned Random Forest was selected as the final Champion Model for mushroom yield prediction.
