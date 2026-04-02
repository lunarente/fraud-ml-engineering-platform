import joblib
from src.preprocess import preprocess_input

model = joblib.load("models/random_forest.pkl")
feature_columns = joblib.load("models/feature_columns.pkl")
scaler = joblib.load("models/scaler.pkl")

def predict_fraud(input_data: dict):
    X = preprocess_input(input_data, feature_columns)

    prediction = model.predict(X)[0]
    probability = model.predict_proba(X)[0][1]

    return {
        "prediction": int(prediction),
        "fraud_probability": float(probability)
    }

