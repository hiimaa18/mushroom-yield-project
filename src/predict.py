import json
import joblib
import pandas as pd

model = joblib.load(
    "models/linear_regression.joblib"
)

with open(
    "models/feature_cols.json",
    "r"
) as f:
    feature_cols = json.load(f)


def predict_yield(
    temperature,
    humidity,
    co2
):

    temp_humidity_interaction = (
        temperature * humidity
    )

    X = pd.DataFrame([{
        "temperature": temperature,
        "humidity": humidity,
        "co2": co2,
        "temp_humidity_interaction":
            temp_humidity_interaction
    }])

    X = X[feature_cols]

    prediction = model.predict(X)[0]

    return float(prediction)


if __name__ == "__main__":

    prediction = predict_yield(
        temperature=24,
        humidity=85,
        co2=650
    )

    print(
        f"\nPredicted Yield: {prediction:.2f} kg"
    )