# Exploratory Data Analysis (EDA) Summary

# Objective

The objective of this exploratory data analysis was to study relationships between environmental variables and mushroom yield using descriptive statistics and visualizations.

The analysis focused on temperature, humidity, CO₂ concentration, and harvested mushroom yield.

---

# Dataset Overview

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

# EDA Visualizations

The following visualizations were created and stored inside `reports/figures/`:

* Correlation heatmap
* Humidity vs Yield scatter plot
* Temperature vs Yield scatter plot
* CO₂ vs Yield scatter plot

All plots include labeled axes with units for readability.

---

# Key Insights

* Humidity values are concentrated around the expected mushroom cultivation range (85–90%).
* Mean and median values are close for all variables, indicating relatively balanced distributions.
* Temperature conditions appear stable across observations, suggesting controlled polyhouse environments.
* Scatter plots suggest environmental conditions may influence mushroom yield patterns.
* CO₂ concentration shows moderate variation and may affect mushroom fruiting behavior.
* Yield variation exists but remains relatively small in the current dataset.

---

# Correlation Interpretation

* Positive correlations indicate variables increasing together.
* Negative correlations indicate inverse relationships.
* Correlation does not necessarily imply biological causation.

The heatmap helps identify potentially important variables for future machine learning models.

---

# Modeling Implications

* Temperature, humidity, and CO₂ can be considered candidate features for predictive modeling.
* Scatter plots should be reviewed for nonlinear relationships before selecting machine learning algorithms.
* Stable environmental conditions may improve prediction consistency.

---

# Conclusion

The exploratory analysis indicates that the cleaned dataset is suitable for further machine learning experimentation.

Environmental variables remain within realistic agricultural ranges and visualizations provide initial insights into possible yield relationships.
