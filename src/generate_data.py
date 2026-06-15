import pandas as pd
import random

rows = []

for _ in range(200):
    temperature = round(random.uniform(22, 27), 1)
    humidity = random.randint(80, 94)
    co2 = random.randint(570, 690)

    # Simple realistic relationship
    yield_kg = round(
        0.4 * temperature +
        0.08 * humidity +
        0.01 * co2 -
        2 +
        random.uniform(-0.5, 0.5),
        1
    )

    rows.append([temperature, humidity, co2, yield_kg])

df = pd.DataFrame(
    rows,
    columns=["temperature", "humidity", "co2", "yield"]
)

df.to_csv("data/raw/mushroom_yield.csv", index=False)

print("Created 200 rows.")