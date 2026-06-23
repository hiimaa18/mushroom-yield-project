import streamlit as st
import joblib
import pandas as pd
import os
from datetime import datetime


def load_artifacts():
    try:
        model = joblib.load(
            "models/champion.joblib"
        )

        scaler = joblib.load(
            "models/minmax_scaler.pkl"
        )

        return model, scaler

    except FileNotFoundError:
        st.error(
            "Model files not found. Please check deployment files."
        )
        st.stop()


model, scaler = load_artifacts()

st.title("🍄 Mushroom Yield Forecast App")

st.write(
    "Predict mushroom yield using environmental sensor values."
)

# Model Information
with st.expander("Model Information"):
    st.write("Champion Model: Tuned Random Forest")
    st.write("Features Used:")
    st.write("- Temperature")
    st.write("- Humidity")
    st.write("- CO₂")
    st.write("- Temp × Humidity")

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

# Out-of-range warnings
if temperature < 20 or temperature > 30:
    st.warning(
        "Temperature is outside the typical training range."
    )

if humidity < 70 or humidity > 95:
    st.warning(
        "Humidity is outside the typical training range."
    )

if co2 < 600 or co2 > 900:
    st.warning(
        "CO₂ is outside the typical training range."
    )

if st.button("Predict Yield"):

    temp_humidity = temperature * humidity

    X = pd.DataFrame([{
        "temperature": temperature,
        "humidity": humidity,
        "co2": co2,
        "temp_humidity": temp_humidity
    }])

    X = X[
        [
            "temperature",
            "humidity",
            "co2",
            "temp_humidity"
        ]
    ]

    X_scaled = scaler.transform(X)

    # Spinner
    with st.spinner("Generating prediction..."):
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

    # Create logs folder automatically
    os.makedirs(
        "logs",
        exist_ok=True
    )

    # Prediction Logging
    log_data = pd.DataFrame([{
        "timestamp": datetime.now(),
        "temperature": temperature,
        "humidity": humidity,
        "co2": co2,
        "predicted_yield": prediction
    }])

    log_file = "logs/prediction_log.csv"

    if os.path.exists(log_file):
        log_data.to_csv(
            log_file,
            mode="a",
            header=False,
            index=False
        )
    else:
        log_data.to_csv(
            log_file,
            index=False
        )

    st.info(
        "Prediction logged successfully."
    )

    # Input Chart
    st.subheader(
        "Current Input Values"
    )

    chart_data = pd.DataFrame({
        "Feature": [
            "Temperature",
            "Humidity",
            "CO₂"
        ],
        "Value": [
            temperature,
            humidity,
            co2
        ]
    })

    st.bar_chart(
        chart_data.set_index(
            "Feature"
        )
    )