import streamlit as st
import joblib
import pandas as pd


def load_artifacts():

    model = joblib.load(
        "models/champion.joblib"
    )

    scaler = joblib.load(
        "models/minmax_scaler.pkl"
    )

    return model, scaler


model, scaler = load_artifacts()

st.title("🍄 Mushroom Yield Forecast App")

st.write(
    "Predict mushroom yield using environmental sensor values."
)

st.sidebar.header("Sensor Inputs")

temperature = st.sidebar.slider(
    "Temperature (°C)",
    min_value=15.0,
    max_value=35.0,
    value=25.0,
    step=0.1
)

humidity = st.sidebar.slider(
    "Humidity (%)",
    min_value=50.0,
    max_value=100.0,
    value=88.0,
    step=0.1
)

co2 = st.sidebar.slider(
    "CO₂ (ppm)",
    min_value=300,
    max_value=1500,
    value=720,
    step=10
)

if st.button("Predict Yield"):

    temp_humidity = temperature * humidity

    X = pd.DataFrame([{
        "temperature": temperature,
        "humidity": humidity,
        "co2": co2,
        "temp_humidity": temp_humidity
    }])

    # Exact column order used during training
    X = X[
        [
            "temperature",
            "humidity",
            "co2",
            "temp_humidity"
        ]
    ]

    X_scaled = scaler.transform(X)

    prediction = model.predict(
        X_scaled
    )[0]

    st.metric(
        label="Predicted Yield",
        value=f"{prediction:.2f} kg"
    )

    st.success(
        "Prediction completed successfully."
    )