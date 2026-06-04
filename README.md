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

# Future Scope

* Exploratory Data Analysis (EDA)
* Machine Learning model training
* Yield prediction
* Environmental trend analysis
* Dashboard visualization

## Author
Hima S
