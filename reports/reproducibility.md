# Reproducibility Note

Champion Model:

* Linear Regression

Artifacts:

* models/linear_regression.joblib
* models/scaler.joblib
* models/feature_cols.json

Random Seed:

* 42 (used where applicable)

Dependencies:

* Python 3.10
* pandas
* numpy
* scikit-learn
* matplotlib
* joblib

To reproduce:

1. Create virtual environment.
2. Install dependencies using:

pip install -r requirements.txt

3. Run:

python src/predict.py

to generate a sample yield prediction.
