# Linear Regression Coefficient Interpretation

The Linear Regression model was trained using scaled environmental features to predict mushroom yield.

| Feature       | Coefficient | Interpretation                                                                                                                                                                                                    |
| ------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Temperature   | -0.0321     | Temperature shows a very small negative relationship with mushroom yield in this dataset. Changes in temperature appear to have limited influence compared to other features.                                     |
| Humidity      | 0.0226      | Humidity has a small positive relationship with yield, suggesting that higher humidity may slightly support mushroom production under the observed conditions.                                                    |
| CO₂           | -0.7118     | CO₂ has the largest coefficient magnitude and shows a negative relationship with yield. Within this dataset, higher CO₂ levels were associated with lower mushroom yield when other variables were held constant. |
| Temp_Humidity | -0.0916     | The interaction between temperature and humidity shows a small negative relationship with yield, indicating that their combined effect may not always improve production.                                         |

## Key Findings

* CO₂ appears to be the most influential feature in the model because it has the largest coefficient magnitude.
* Humidity shows a slight positive association with mushroom yield.
* Temperature and the temperature-humidity interaction have relatively small negative coefficients.
* Since MinMaxScaler was applied, coefficient values represent relative feature influence rather than direct physical unit changes.

## Important Limitation

The dataset contains only 6 observations, with 2 observations in the test set. Therefore, coefficient interpretations should be considered preliminary and may change as additional data becomes available.

## Baseline Assessment

The model achieved:

* MAE = 0.256
* RMSE = 0.349
* R² = 0.598

An R² value of approximately 0.60 indicates that the model explains about 60% of the variation in mushroom yield. This is acceptable as a baseline model and provides a reference point for future comparison with more advanced models such as Random Forest Regression.

