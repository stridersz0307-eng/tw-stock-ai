from pathlib import Path

import pandas as pd


def load_stock_list(path: str | Path) -> pd.DataFrame:
    """Load stock IDs from a one-column CSV file."""
    stock_df = pd.read_csv(path, header=None, names=["stock_id"], dtype=str)
    stock_df["stock_id"] = stock_df["stock_id"].str.strip()
    return stock_df[stock_df["stock_id"].ne("")].reset_index(drop=True)


def load_price_data(stock_id: str, periods: int = 120) -> pd.DataFrame:
    """Generate deterministic sample close price data for a stock.

    This MVP uses synthetic data so the project runs without external APIs.
    """
    end_date = pd.Timestamp.today().normalize()
    dates = pd.bdate_range(end=end_date, periods=periods)

    base_price = 50 + (sum(ord(ch) for ch in stock_id) % 100)
    trend = pd.Series(range(periods), dtype=float) * 0.15
    seasonal = pd.Series([((i % 10) - 5) * 0.4 for i in range(periods)], dtype=float)

    close = base_price + trend + seasonal
    return pd.DataFrame({"date": dates, "close": close})
