# Monitoring Plan

## Objective

Monitor prediction requests and identify situations where model retraining may be required.

---

## Prediction Logging

For each prediction request, the following information should be recorded:

* Timestamp
* Temperature
* Humidity
* CO₂
* Predicted Yield

Example:

| Timestamp        | Temperature | Humidity | CO₂ | Predicted Yield |
| ---------------- | ----------- | -------- | --- | --------------- |
| 2026-06-19 14:00 | 25          | 88       | 720 | 12.22 kg        |

---

## Monitoring Goals

The monitoring process aims to:

1. Detect unusual sensor values.
2. Identify prediction drift.
3. Track application usage.
4. Support future model retraining.

---

## Retraining Triggers

Model retraining should be considered when:

* New sensor data becomes available.
* Prediction errors increase significantly.
* Seasonal growing conditions change.
* Environmental values fall outside the original training range.

---

## Artifact Management

The following artifacts are stored within the repository:

* models/champion.joblib
* models/minmax_scaler.pkl
* models/feature_cols.json

These artifacts are loaded during application startup and used for all predictions.

---

## Future Improvements

* Automated logging database
* Performance monitoring dashboard
* Scheduled model retraining
* Cloud-based storage for prediction history

---

## Conclusion

A lightweight monitoring strategy was implemented to track model predictions and support future maintenance of the mushroom yield forecasting system.
