# Data Quality Report

## Overview

This report summarizes the statistical characteristics and quality metrics of the cleaned mushroom polyhouse dataset.

The goal is to understand environmental sensor behavior and evaluate whether the dataset is suitable for future machine learning analysis.

---

# Dataset Summary

| Metric             | Value               |
| ------------------ | ------------------- |
| Total Observations | 6                   |
| Number of Columns  | 5                   |
| Start Date         | 2026-06-01 08:00:00 |
| End Date           | 2026-06-02 16:00:00 |

---

# Summary Statistics

| Column      | Mean   | Median | Std Dev | Min    | Max    |
| ----------- | ------ | ------ | ------- | ------ | ------ |
| Temperature | 24.67  | 24.65  | 0.95    | 23.50  | 26.20  |
| Humidity    | 87.17  | 87.50  | 3.31    | 82.00  | 91.00  |
| CO₂         | 725.00 | 715.00 | 44.16   | 680.00 | 800.00 |
| Yield (kg)  | 12.45  | 12.45  | 0.41    | 11.90  | 13.00  |

---

# Data Quality Metrics

| Rule                       | Pass Percentage |
| -------------------------- | --------------- |
| Humidity between 0–100%    | 100%            |
| CO₂ greater than 0         | 100%            |
| Temperature between 0–50°C | 100%            |

---

# Observations & Insights

* Humidity values are concentrated around the 85–90% range, which is suitable for mushroom cultivation environments.
* Mean and median values are very close for all variables, indicating balanced distributions with minimal skew.
* Yield values show small variation, suggesting a relatively stable production environment.
* All rows passed environmental validity checks after data cleaning.
* Temperature variation is low, indicating controlled polyhouse conditions.

---

# Chronological Train/Test Split

To prevent data leakage, the dataset was sorted by timestamp and split chronologically. Earlier observations were used for training and later observations were reserved for testing.

## Split Details

| Metric           | Value                       |
| ---------------- | --------------------------- |
| Split Strategy   | Chronological (Time-Series) |
| Train Size       | 4 rows                      |
| Test Size        | 2 rows                      |
| Train Percentage | 80%                         |
| Test Percentage  | 20%                         |

## Train Period

| Start Date          | End Date            |
| ------------------- | ------------------- |
| 2026-06-01 08:00:00 | 2026-06-02 08:00:00 |

## Test Period

| Start Date          | End Date            |
| ------------------- | ------------------- |
| 2026-06-02 12:00:00 | 2026-06-02 16:00:00 |

## Scaling Procedure

A MinMaxScaler was fitted using only the training dataset to prevent information leakage from future observations.

The fitted scaler was then used to transform both training and testing feature sets.

## Leakage Prevention Verification

* Dataset sorted by timestamp before splitting.
* Training observations occur strictly before testing observations.
* No future information was used when creating features.
* Test data was transformed using statistics learned from training data only.


# Conclusion

The cleaned dataset demonstrates acceptable quality for exploratory analysis and future predictive modeling tasks.

Environmental sensor readings remain within expected agricultural ranges and the dataset appears consistent after cleaning.
