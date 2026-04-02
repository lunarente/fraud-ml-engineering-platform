from pathlib import Path
import joblib
import pandas as pd


def get_models_dir():
    return Path(__file__).resolve().parents[2] / "models"


def load_pipeline():
    models_dir = get_models_dir()
    return joblib.load(models_dir / "fraud_detection_pipeline.joblib")


pipeline = load_pipeline()


def predict_transaction(data: pd.DataFrame):
    proba = pipeline.predict_proba(data)[:, 1]
    prediction = (proba > 0.5).astype(int)

    return prediction, proba