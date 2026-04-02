import numpy as np
import pandas as pd


def add_log_amount_feature(X: pd.DataFrame) -> pd.DataFrame:
    X = X.copy()
    X["log_amount"] = np.log1p(X["Amount"])
    X = X.drop(columns=["Amount"])
    return X


def basic_data_check(df: pd.DataFrame) -> dict:
    return {
        "n_rows": df.shape[0],
        "n_cols": df.shape[1],
        "missing_values": int(df.isnull().sum().sum()),
        "fraud_count": int(df["Class"].sum()),
        "fraud_ratio": float(df["Class"].mean())
    }