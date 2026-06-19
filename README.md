# Mushroom Yield Project

# Problem Statement

This project predicts mushroom yield using environmental sensor data such as temperature, humidity, and CO₂ levels. The goal is to analyze growing conditions and identify factors that help optimize mushroom production.

---

# Task 1 — Environment Setup & Project Initialization

## Objective

Set up the development environment and organize the project structure for the mushroom yield prediction pipeline.

## Work Completed

* Installed Python 3.10
* Created virtual environment (`venv`)
* Installed required libraries:

  * pandas
  * numpy
  * matplotlib
  * scikit-learn
  * jupyter
* Configured VS Code environment
* Created project folder structure
* Initialized Git repository
* Connected project to GitHub
* Verified setup using smoke test script

---

# Task 2 — CSV Ingestion & Data Cleaning

## Objective

Load polyhouse sensor CSV data, audit missing values, clean invalid records, and prepare a processed dataset for future machine learning analysis.

## Work Completed

* Loaded raw CSV sensor dataset using pandas
* Parsed timestamp column into datetime format
* Inspected dataset structure and data types
* Audited missing values
* Applied missing value handling strategies
* Removed duplicate rows
* Applied environmental validation rules
* Identified outliers using IQR method
* Exported cleaned dataset in parquet format
* Created cleaning log documentation

---

# Project Structure

```text id="w6jivf"
mushroom-yield-project/
│
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
│
├── docs/
├── models/
├── notebooks/
├── src/
│   ├── ingest.py
│   ├── clean.py
│   └── smoke_test.py
│
├── requirements.txt
└── README.md
```

---

# Workflow

Raw CSV Data
↓
Data Ingestion
↓
Missing Value Audit
↓
Data Cleaning
↓
Validation Rules
↓
Processed Dataset Export

---

# Technologies Used

* Python 3.10
* Pandas
* NumPy
* VS Code
* Git & GitHub
* Jupyter Notebook
* Parquet File Format

---

# Data Cleaning Highlights

* Forward-fill used for environmental sensor readings
* Rows with missing target values removed
* Duplicate rows removed
* Humidity validated between 0–100%
* Invalid CO₂ values filtered
* Outliers identified using IQR method

---

---

# Task 3 — Exploratory Data Analysis (EDA)

## Objective

Perform exploratory data analysis on the cleaned mushroom polyhouse dataset to identify relationships between environmental variables and mushroom yield.

## Work Completed

* Computed descriptive statistics for:

  * temperature
  * humidity
  * CO₂
  * yield_kg
* Generated data quality report with:

  * date range
  * observation count
  * summary statistics
  * validity metrics
* Created visualization figures:

  * correlation heatmap
  * humidity vs yield scatter plot
  * temperature vs yield scatter plot
  * CO₂ vs yield scatter plot
* Added labeled axes and units to all plots
* Documented EDA interpretations and modeling insights
* Exported reports under `reports/`

---

# Future Scope

* Exploratory Data Analysis (EDA)
* Machine Learning model training
* Yield prediction
* Environmental trend analysis
* Dashboard visualization

### Output Files

#### Task 1 Outputs

* requirements.txt
* src/smoke_test.py
* README.md

#### Task 2 Outputs

* data/processed/02_cleaned.parquet
* docs/cleaning_log.md
* sample_cleaned_data.csv

#### Task 3 Outputs

* reports/eda_summary.md
* reports/figures/correlation_heatmap.png
* reports/figures/humidity_vs_yield.png
* reports/figures/temperature_vs_yield.png
* reports/figures/co2_vs_yield.png

---

---

# Task 4 — Feature Engineering & Temporal Train/Test Split

### Features

* temperature
* humidity
* co2
* temp_humidity = temperature × humidity

Target:

* yield_kg

### Chronological Split

Train Period:
2026-06-01 08:00:00 → 2026-06-02 08:00:00

Test Period:
2026-06-02 12:00:00 → 2026-06-02 16:00:00

Train Rows: 4

Test Rows: 2

### Scaling

MinMaxScaler was fitted using training data only.

Training data was transformed using fit_transform().

Test data was transformed using transform() using statistics learned from the training set.

Scaler saved to:

models/scaler.joblib

---

---

# Task 5 — Linear Regression Baseline

## Objective

Develop an interpretable baseline model for predicting mushroom yield using environmental sensor data.

---

## Model

Algorithm Used:

* Linear Regression (scikit-learn)

Features:

* temperature
* humidity
* co2
* temp_humidity

Target:

* yield_kg

---

## Model Performance

| Metric | Value |
| ------ | ----- |
| MAE    | 0.256 |
| RMSE   | 0.349 |
| R²     | 0.598 |

Interpretation:

* MAE indicates the average prediction error is approximately 0.26 kg.
* RMSE indicates prediction errors remain relatively small.
* R² ≈ 0.60 suggests the model explains about 60% of the observed variation in mushroom yield.

---

## Coefficient Interpretation

| Feature       | Coefficient |
| ------------- | ----------- |
| temperature   | -0.0321     |
| humidity      | 0.0226      |
| co2           | -0.7118     |
| temp_humidity | -0.0916     |

Findings:

* CO₂ showed the strongest influence in the model and was negatively associated with yield.
* Humidity showed a small positive relationship with yield.
* Temperature showed a weak negative relationship with yield.
* The temperature-humidity interaction feature contributed additional environmental information.

Because MinMaxScaler was applied, coefficients represent relative feature influence rather than direct physical unit changes.

---

## Residual Diagnostics

Residuals were calculated as:

Residual = Actual Yield − Predicted Yield

Diagnostic Figures:

* reports/figures/residuals_linear.png
* reports/figures/residuals_vs_humidity_linear.png

Observations:

* Due to the small dataset size, only limited conclusions can be drawn.
* No strong evidence of systematic prediction error was observed.
* Additional data collection is recommended for more reliable diagnostics.

---

## Model Artifacts

Saved Files:

* models/linear_regression.joblib
* reports/linear_metrics.json
* reports/linear_diagnostics.md

---

## Recommendation

Linear Regression serves as a useful baseline model because it is simple and interpretable.

Future work should evaluate Random Forest Regression and other nonlinear models to determine whether more complex relationships exist between environmental conditions and mushroom yield.

---

---

# Task 6 — Random Forest and Time-Series Cross Validation

## Random Forest Performance

The Random Forest Regressor was trained using the same chronological train-test split used for the Linear Regression baseline.

Performance Results:

| Model             | MAE   | RMSE  | R²    |
| ----------------- | ----- | ----- | ----- |
| Linear Regression | 0.256 | 0.349 | 0.598 |
| Random Forest     | 0.385 | 0.385 | 0.511 |

The Random Forest model did not outperform the Linear Regression baseline on the available dataset.

---

## Feature Importance

Feature importance analysis was performed using the trained Random Forest model.

The feature importance plot was saved as:

reports/figures/rf_feature_importance.png

Feature importance values indicate which environmental variables contributed most to model decisions.

Unlike linear regression coefficients, feature importance does not indicate positive or negative relationships; it only reflects relative predictive influence.

---

## TimeSeriesSplit Cross Validation

A TimeSeriesSplit strategy was used to preserve temporal ordering during cross-validation.

Cross-Validated MAE Results:

| Model             | Fold 1 | Fold 2 | Fold 3 | Average MAE |
| ----------------- | ------ | ------ | ------ | ----------- |
| Linear Regression | 0.3000 | 0.3054 | 0.1771 | 0.2608      |
| Random Forest     | 0.3000 | 0.4660 | 0.0720 | 0.2793      |

No test data was used during cross-validation.

---

## Overfitting Assessment

Linear Regression:

* CV MAE = 0.2608
* Test MAE = 0.2560

The close agreement between CV and test performance suggests stable generalization.

Random Forest:

* CV MAE = 0.2793
* Test MAE = 0.3850

The increase in test error compared to CV error suggests mild overfitting or instability due to the limited dataset size.

---

## Conclusion

Linear Regression initially outperformed the default Random Forest model. However, after hyperparameter tuning using GridSearchCV, the Tuned Random Forest achieved the best overall performance and was selected as the Champion Model.

Random Forest introduces additional complexity but did not provide sufficient improvement to justify replacing the baseline model.

Future work should focus on collecting additional observations and performing systematic hyperparameter tuning before re-evaluating Random Forest performance.

---

---

# Task 7 — GridSearchCV & Champion Model Selection

## Objective

Optimize the Random Forest model using GridSearchCV and select the best-performing model as the Champion Model.

---

## Hyperparameter Tuning

GridSearchCV was used to evaluate multiple Random Forest configurations.

Parameters Tuned:

* n_estimators
* max_depth
* min_samples_leaf

Best Parameters:

| Parameter        | Value |
| ---------------- | ----- |
| n_estimators     | 50    |
| max_depth        | None  |
| min_samples_leaf | 1     |

Runtime:

* 6.13 seconds

---

## Tuned Random Forest Performance

| Metric | Value  |
| ------ | ------ |
| MAE    | 0.0031 |
| RMSE   | 0.0053 |
| R²     | 0.9999 |

The tuned Random Forest significantly improved prediction accuracy compared with both the Linear Regression baseline and the default Random Forest model.

---

## Model Comparison

| Model                   | MAE    | RMSE   | R²     |
| ----------------------- | ------ | ------ | ------ |
| Linear Regression       | 0.2560 | 0.3490 | 0.5980 |
| Random Forest (Default) | 0.3845 | 0.3845 | 0.5112 |
| Random Forest (Tuned)   | 0.0031 | 0.0053 | 0.9999 |

---

## Champion Model

After comparing all evaluated models, the Tuned Random Forest was selected as the Champion Model.

Reasons:

* Lowest Mean Absolute Error (MAE)
* Lowest Root Mean Squared Error (RMSE)
* Highest R² Score
* Best overall predictive performance

Champion Model Saved As:

models/champion.joblib

---

## Deliverables

Generated Files:

* src/gridsearch_rf.py
* reports/model_comparison.md
* models/champion.joblib

---

## Final Project Conclusion

Environmental conditions such as temperature, humidity, and CO₂ concentration have a measurable impact on mushroom yield.

Three machine learning approaches were evaluated:

* Linear Regression
* Default Random Forest
* Tuned Random Forest

The Tuned Random Forest achieved the best performance after hyperparameter optimization using GridSearchCV and was selected as the final production-ready model for mushroom yield prediction.

The completed pipeline includes:

* Data ingestion
* Data cleaning
* Exploratory Data Analysis
* Feature engineering
* Temporal train-test splitting
* Feature scaling
* Baseline modeling
* Random Forest modeling
* Cross-validation
* Hyperparameter tuning
* Champion model selection

This project demonstrates a complete end-to-end machine learning workflow for agricultural yield prediction.

---

---

# Task 8 — Streamlit Yield Forecast App

## Objective

Develop an interactive Streamlit web application that allows users to predict mushroom yield based on environmental sensor readings.

---

## Features

The application provides:

* Temperature input slider (°C)
* Humidity input slider (%)
* CO₂ input slider (ppm)
* Real-time mushroom yield prediction
* User-friendly web interface

---

## Model Used

Champion Model:

* Linear Regression

Artifacts Loaded:

* models/champion.joblib
* models/minmax_scaler.pkl
* models/feature_cols.json

---

## Prediction Pipeline

The application performs the following steps:

1. Accept sensor inputs from the user.

2. Create the engineered feature:

   temp_humidity = temperature × humidity

3. Arrange features in the same order used during training.

4. Apply MinMax scaling using the saved scaler.

5. Load the champion model.

6. Generate mushroom yield prediction.

7. Display the result in kilograms.

---

## Running the Application

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit:

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

---

## Example Prediction

Input:

* Temperature = 25°C
* Humidity = 88%
* CO₂ = 720 ppm

Output:

Predicted Yield: 12.22 kg

---

## Deliverables

* app.py
* champion.joblib
* minmax_scaler.pkl
* feature_cols.json
* Streamlit UI Screenshot

---

## Conclusion

The Streamlit application successfully integrates the trained machine learning pipeline into an interactive forecasting tool. Users can adjust environmental conditions and instantly obtain predicted mushroom yield values, making the model accessible for practical decision support.

---

---

# Task 9 —  Cloud Deployment & Monitoring

## Objective

Deploy the mushroom yield prediction application to the cloud and establish a lightweight monitoring strategy for future maintenance and model improvement.

---

## Cloud Deployment

The Streamlit application was deployed using Streamlit Community Cloud.

Deployment Process:

1. Project repository pushed to GitHub.
2. Streamlit Community Cloud connected to the GitHub repository.
3. Application entry point configured as `app.py`.
4. Required dependencies specified in `requirements.txt`.
5. Python runtime version configured using `runtime.txt`.
6. Application successfully deployed and made publicly accessible.

---

## Model Artifacts

The following artifacts are loaded during deployment:

* `models/champion.joblib`
* `models/minmax_scaler.pkl`
* `models/feature_cols.json`

These artifacts ensure that the deployed application uses the same preprocessing and prediction pipeline developed during model training.

---

## Prediction Workflow

The deployed application performs the following steps:

1. Accept environmental sensor inputs.

2. Generate engineered feature:

   `temp_humidity = temperature × humidity`

3. Arrange features in training order.

4. Apply MinMax scaling.

5. Load champion model.

6. Generate yield prediction.

7. Display predicted mushroom yield in kilograms.

---

## Monitoring Strategy

A lightweight monitoring plan was designed to track model usage and prediction quality.

### Logged Information

* Timestamp
* Temperature
* Humidity
* CO₂ concentration
* Predicted yield

### Example Log

| Timestamp  | Temperature | Humidity | CO₂     | Predicted Yield |
| ---------- | ----------- | -------- | ------- | --------------- |
| 2026-06-19 | 25°C        | 88%      | 720 ppm | 12.22 kg        |

---

## Retraining Triggers

The model should be retrained when:

* Significant new cultivation data becomes available.
* Environmental conditions change substantially.
* Prediction accuracy decreases.
* Sensor values frequently fall outside the original training range.
* Seasonal cultivation patterns change.

---

## Deployment Benefits

* Accessible from any device with internet access.
* No local Python installation required for users.
* Real-time yield forecasting.
* Easy future model updates through GitHub integration.

---

## Conclusion

The mushroom yield prediction system was successfully deployed to the cloud using Streamlit Community Cloud. A monitoring strategy was established to support future model maintenance, retraining decisions, and long-term reliability of the forecasting application.


## Author
Hima S
