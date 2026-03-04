import pandas as pd


def compute_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """Compute MA5, MA20, MA60, and RSI(14) indicators."""
    result = df.copy()

    result["MA5"] = result["close"].rolling(window=5, min_periods=5).mean()
    result["MA20"] = result["close"].rolling(window=20, min_periods=20).mean()
    result["MA60"] = result["close"].rolling(window=60, min_periods=60).mean()

    delta = result["close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=14, min_periods=14).mean()
    avg_loss = loss.rolling(window=14, min_periods=14).mean()

    rs = avg_gain / avg_loss.replace(0, pd.NA)
    result["RSI14"] = 100 - (100 / (1 + rs))

    return result
