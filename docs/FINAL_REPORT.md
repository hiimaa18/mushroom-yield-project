# Mushroom Yield Prediction Using Environmental Sensor Data

## Final Technical Report

### Author

Hima S

### Project Duration

Internship Capstone Project

---

# 1. Problem Statement

Mushroom cultivation is highly sensitive to environmental conditions such as temperature, humidity, and carbon dioxide concentration. Small changes in these variables can significantly affect mushroom growth and final yield.

The objective of this project was to develop a machine learning system capable of predicting mushroom yield using environmental sensor readings. The solution aims to assist growers in understanding environmental impacts on production and support data-driven cultivation decisions.

---

# 2. Dataset Description

The dataset contains polyhouse environmental sensor readings collected over time.

Features:

* Temperature (°C)
* Humidity (%)
* CO₂ Concentration (ppm)

Target Variable:

* Mushroom Yield (kg)

Each observation represents environmental conditions associated with a harvested yield value.

---

# 3. Data Ingestion and Cleaning

The dataset was imported using the Pandas library.

Data quality checks included:

* Missing value detection
* Duplicate record removal
* Data type verification
* Environmental validity checks

Validation rules:

* Humidity between 0–100%
* CO₂ greater than 0
* Temperature within realistic cultivation limits

After cleaning, a processed dataset was generated for analysis and modeling.

---

# 4. Exploratory Data Analysis (EDA)

EDA was performed to understand feature distributions and relationships with mushroom yield.

Analysis included:

* Summary statistics
* Correlation analysis
* Scatter plots
* Data quality reporting

Key Findings:

* Humidity remained within cultivation-friendly ranges.
* Temperature showed limited variation due to controlled conditions.
* Yield values were relatively stable.
* No significant data quality issues remained after cleaning.

---

# 5. Feature Engineering

Machine learning features were prepared using environmental variables.

Input Features:

* Temperature
* Humidity
* CO₂

Target Variable:

* Yield (kg)

An additional interaction feature was created:

temp_humidity = temperature × humidity

This feature was introduced to capture the combined influence of temperature and humidity on mushroom growth.

Feature scaling was performed using MinMaxScaler.

---

# 6. Temporal Train-Test Split

Because the dataset represents time-based observations, a chronological train-test split was implemented.

Split Strategy:

* 80% Training Data
* 20% Testing Data

The dataset was sorted by timestamp before splitting.

To avoid data leakage:

* The scaler was fitted only on training data.
* Test data was transformed using the training scaler.

This approach simulates real-world future prediction scenarios.

---

# 7. Linear Regression Baseline

A Linear Regression model was trained as the baseline model.

Evaluation Metrics:

* MAE
* RMSE
* R² Score

Results:

* MAE = 0.256
* RMSE = 0.349
* R² = 0.598

Residual analysis was conducted to identify prediction patterns and model limitations.

Advantages:

* Easy interpretation
* Fast training
* Transparent coefficients

---

# 8. Random Forest Model

A Random Forest Regressor was trained to capture nonlinear relationships between environmental conditions and yield.

Model Characteristics:

* Ensemble of decision trees
* Handles feature interactions automatically
* Reduced sensitivity to outliers

Feature importance analysis was performed to determine the influence of environmental variables.

---

# 9. Time-Series Cross Validation

TimeSeriesSplit was used for model validation.

Reasons:

* Preserves chronological order
* Prevents future information leakage
* Provides realistic performance estimation

Cross-validation scores were used to evaluate model stability and detect overfitting.

---

# 10. Hyperparameter Tuning

GridSearchCV was used to optimize Random Forest parameters.

Parameters Tuned:

* n_estimators
* max_depth
* min_samples_leaf

Best Parameters:

* n_estimators = 50
* max_depth = 2
* min_samples_leaf = 1

The tuned model was evaluated on the untouched test set.

---

# 11. Model Comparison

| Model               | MAE    | RMSE   | R²     |
| ------------------- | ------ | ------ | ------ |
| Linear Regression   | 0.256  | 0.349  | 0.598  |
| Random Forest       | 0.385  | 0.385  | 0.511  |
| Tuned Random Forest | 0.0031 | 0.0053 | 0.9999 |

The Linear Regression model provided a strong and interpretable baseline. The default Random Forest model did not outperform the baseline on the available dataset. However, after hyperparameter tuning using GridSearchCV, the Tuned Random Forest achieved significantly improved predictive performance and became the best-performing model.

---

# 12. Champion Model Selection

The Tuned Random Forest model was selected as the Champion Model because it achieved:

* Lowest Mean Absolute Error (MAE)
* Lowest Root Mean Squared Error (RMSE)
* Highest R² Score
* Best overall predictive performance

The model demonstrated superior predictive accuracy compared to both the Linear Regression baseline and the default Random Forest model.

The champion model was saved as:

models/champion.joblib

---

# 13. Deployment

The final model was deployed using Streamlit Community Cloud.

Deployment Components:

* app.py
* champion.joblib
* minmax_scaler.pkl
* feature_cols.json
* requirements.txt

Users can provide environmental sensor values through a web interface and receive real-time yield predictions.

---

# 14. Monitoring Strategy

A lightweight monitoring framework was implemented to track prediction activity and support future model maintenance.

Logged Information:

* Timestamp
* Temperature
* Humidity
* CO₂
* Predicted Yield

Prediction logs are automatically stored in:

logs/prediction_log.csv

These logs provide historical prediction records and can be used to monitor model behavior over time.

Retraining Triggers:

* New cultivation data becomes available.
* Seasonal growing conditions change.
* Prediction accuracy decreases.
* Sensor values frequently fall outside the original training range.
* Environmental patterns differ significantly from training data.

Monitoring prediction trends helps identify potential model drift and determine when retraining is required.

---

# 15. Limitations

The project has several limitations:

* Small dataset size
* Limited environmental variables
* Seasonal effects not fully captured
* Predictions depend on sensor quality
* Limited historical observations

---

# 16. Future Work

Future improvements may include:

* Larger real-world datasets
* Additional sensor variables
* Deep learning models
* Automated retraining pipelines
* Cloud database integration
* Real-time IoT sensor connectivity

---

# 17. Conclusion

This project successfully developed an end-to-end machine learning solution for mushroom yield prediction. The workflow included data cleaning, exploratory analysis, feature engineering, temporal validation, model development, hyperparameter tuning, deployment, and monitoring. The final deployed application demonstrates how environmental sensor data can be transformed into actionable yield forecasts through machine learning.
