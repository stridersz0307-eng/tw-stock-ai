import pandas as pd


def generate_signals(df: pd.DataFrame) -> pd.DataFrame:
    """Generate WATCH and RISK signals from indicator values."""
    result = df.copy()
    result["WATCH"] = result["close"] > result["MA20"]
    result["RISK"] = result["close"] < result["MA60"]
    return result
