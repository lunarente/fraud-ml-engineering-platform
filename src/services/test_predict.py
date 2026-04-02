import pandas as pd
from src.data.load_data import load_raw_data
from src.services.predict import predict_transaction


def main():
    df = load_raw_data()

    sample = df.drop(columns=["Class"]).sample(5, random_state=42)

    prediction, proba = predict_transaction(sample)

    print("Predições:", prediction)
    print("Probabilidades:", proba)


if __name__ == "__main__":
    main()