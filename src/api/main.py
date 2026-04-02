from fastapi import FastAPI
import pandas as pd

from src.schemas.transaction import TransactionInput
from src.services.predict import predict_transaction


app = FastAPI(
    title="Fraud Detection API",
    description="API para predição de fraude em transações de cartão",
    version="1.1"
)


@app.get("/")
def home():
    return {
        "message": "Fraud Detection API running",
        "model": "Random Forest"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "fraud-detection-api"
    }


@app.post("/predict")
def predict(data: TransactionInput):
    df = pd.DataFrame([data.model_dump()])

    prediction, proba = predict_transaction(df)

    fraud_probability = float(proba[0])
    pred = int(prediction[0])

    if fraud_probability >= 0.70:
        risk_level = "high"
    elif fraud_probability >= 0.30:
        risk_level = "moderate"
    else:
        risk_level = "low"

    return {
        "fraud_probability": fraud_probability,
        "prediction": pred,
        "prediction_label": "fraud" if pred == 1 else "normal",
        "risk_level": risk_level
    }