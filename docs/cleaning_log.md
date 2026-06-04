# Data Cleaning Log

## Objective

Clean the mushroom polyhouse sensor dataset before machine learning.

---

## Missing Value Strategy

### Sensor Columns

Columns:

* temperature
* humidity
* co2

Used forward-fill because sensor values are time-series readings and nearby values are usually similar.

### Target Column

Column:

* yield_kg

Rows with missing target values were removed.

Reason:
Target values should never be imputed because it can cause label leakage.

### Remaining Numeric Columns

Filled using median values to reduce effect of extreme outliers.

---

## Duplicate Handling

Removed duplicate rows using pandas `drop_duplicates()`.

Duplicate timestamps can distort time-series analysis and yield averages.

---

## Validity Rules

Applied the following filtering rules:

* humidity must be between 0 and 100
* co2 must be greater than 0
* temperature must be between 0 and 50

Rows violating these conditions were removed.

---

## Outlier Handling

Outliers were detected using the IQR method.

Outliers were flagged for review but not automatically deleted because unusual environmental readings may still be agriculturally meaningful.

---

## Final Checks

* Final cleaned dataset exported as `02_cleaned.parquet`
* Verified target column has zero missing values
* Documented row removal and cleaning strategy
