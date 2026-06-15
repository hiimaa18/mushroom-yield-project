# Model Comparison

| Model                   | CV MAE | Test MAE | RMSE   | R²     |
| ----------------------- | ------ | -------- | ------ | ------ |
| Linear Regression       | 0.2608 | 0.2560   | 0.3490 | 0.5980 |
| Random Forest (Default) | 0.2793 | 0.3850   | 0.3850 | 0.5110 |
| Random Forest (Tuned)   | 0.2793 | 0.3920   | 0.3920 | 0.4920 |

---

## Champion Model

### Selected Model

Linear Regression

### Justification

Linear Regression achieved:

* Lowest MAE
* Lowest RMSE
* Highest R²
* Most stable cross-validation performance

The Random Forest models did not improve performance despite hyperparameter tuning.

Because the dataset is very small, the simpler Linear Regression model generalized better than the more complex Random Forest models.

---

## Final Recommendation

Linear Regression is selected as the champion model for deployment.

The model provides the best balance of:

* Accuracy
* Stability
* Interpretability

and is therefore the preferred choice for the mushroom yield prediction system.
