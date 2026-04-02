from pathlib import Path
import pandas as pd


def get_project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def load_raw_data(filename: str = "creditcard.csv") -> pd.DataFrame:
    root = get_project_root()
    file_path = root / "data" / "raw" / filename

    if not file_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

    df = pd.read_csv(file_path)
    return df