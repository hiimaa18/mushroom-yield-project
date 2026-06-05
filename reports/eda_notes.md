# EDA Notes

## Objective

The objective of this exploratory data analysis was to identify relationships between environmental conditions and mushroom yield.

Visual analysis was performed using scatter plots and correlation heatmaps.

---

# Key Observations

* Humidity values are concentrated within the expected mushroom cultivation range (approximately 85–90%).
* Temperature variation appears relatively stable, indicating controlled polyhouse conditions.
* Yield values show moderate variation, which may help machine learning models learn useful patterns.
* Correlation analysis suggests environmental variables may influence mushroom yield differently.
* Scatter plots help identify whether relationships appear linear or nonlinear.

---

# Correlation Insights

* Positive correlations indicate variables that increase together.
* Negative correlations indicate inverse relationships.
* Correlation does not guarantee causation; biological interpretation is still required.

---

# Plot Interpretations

## Humidity vs Yield

The scatter plot helps evaluate whether higher humidity levels are associated with increased mushroom production.

Mushrooms typically require high humidity for proper growth and fruiting.

---

## Temperature vs Yield

The temperature plot helps identify optimal environmental conditions for yield stability.

Extreme temperatures may negatively affect mushroom growth.

---

## CO₂ vs Yield

The CO₂ scatter plot helps analyze whether air quality and ventilation conditions influence harvested yield.

High CO₂ concentrations may affect mushroom fruiting behavior.

---

# Modeling Implications

* Environmental variables appear suitable as candidate features for predictive modeling.
* Scatter plots should be reviewed for nonlinear patterns before selecting machine learning algorithms.
* Correlation analysis may help prioritize important variables during feature selection.
