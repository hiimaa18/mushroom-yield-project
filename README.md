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

## Task 4: Feature Engineering & Temporal Train/Test Split

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

# Task 5: Linear Regression Baseline

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


## Author
Hima S
