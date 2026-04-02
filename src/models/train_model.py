from pathlib import Path
import joblib

from src.data.load_data import load_raw_data
from src.data.preprocess import add_log_amount_feature

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import FunctionTransformer, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)


def get_models_dir() -> Path:
    return Path(__file__).resolve().parents[2] / "models"


def evaluate_classification_model(y_true, y_pred, y_proba):
    metrics = {
        "precision": precision_score(y_true, y_pred),
        "recall": recall_score(y_true, y_pred),
        "f1_score": f1_score(y_true, y_pred),
        "roc_auc": roc_auc_score(y_true, y_proba)
    }
    return metrics


def print_classification_report(y_true, y_pred):
    print("Classification Report:")
    print(classification_report(y_true, y_pred))

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_true, y_pred))


def main():
    print("Carregando dados...")
    df = load_raw_data()

    X = df.drop(columns=["Class"])
    y = df["Class"]

    print("Fazendo train/test split...")
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    print("Criando pipeline...")

    preprocess_pipeline = Pipeline(
        steps=[
            ("log_amount", FunctionTransformer(add_log_amount_feature, validate=False)),
            ("scaler", StandardScaler())
        ]
    )

    pipeline = Pipeline(
        steps=[
            ("preprocessing", preprocess_pipeline),
            (
                "model",
                RandomForestClassifier(
                    n_estimators=200,
                    max_depth=None,
                    class_weight="balanced",
                    n_jobs=-1,
                    random_state=42
                )
            )
        ]
    )

    print("Treinando pipeline...")
    pipeline.fit(X_train, y_train)

    print("Gerando predições...")
    y_pred = pipeline.predict(X_test)
    y_proba = pipeline.predict_proba(X_test)[:, 1]

    print("Calculando métricas...")
    metrics = evaluate_classification_model(y_test, y_pred, y_proba)

    print("\nMétricas do modelo:")
    for key, value in metrics.items():
        print(f"{key}: {value:.4f}")

    print()
    print_classification_report(y_test, y_pred)

    print("\nSalvando pipeline...")
    models_dir = get_models_dir()
    models_dir.mkdir(parents=True, exist_ok=True)

    joblib.dump(pipeline, models_dir / "fraud_detection_pipeline.joblib")

    print(f"Pipeline salvo em: {models_dir / 'fraud_detection_pipeline.joblib'}")


if __name__ == "__main__":
    main()