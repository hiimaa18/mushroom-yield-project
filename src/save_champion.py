import joblib

model = joblib.load(
    "models/linear_regression.joblib"
)

joblib.dump(
    model,
    "models/champion.joblib"
)

print("Champion model saved.")