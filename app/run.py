from pathlib import Path

import pandas as pd

from data_loader import load_price_data, load_stock_list
from indicators import compute_indicators
from signals import generate_signals


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "stock_list.csv"
OUTPUT_DIR = BASE_DIR / "outputs"


def run() -> pd.DataFrame:
    stock_list = load_stock_list(DATA_PATH)
    summaries = []

    for stock_id in stock_list["stock_id"]:
        price_df = load_price_data(stock_id)
        analysis_df = generate_signals(compute_indicators(price_df))

        output_path = OUTPUT_DIR / f"{stock_id}_signals.csv"
        analysis_df.to_csv(output_path, index=False)

        latest = analysis_df.iloc[-1]
        summaries.append(
            {
                "stock_id": stock_id,
                "close": round(float(latest["close"]), 2),
                "MA20": round(float(latest["MA20"]), 2),
                "MA60": round(float(latest["MA60"]), 2),
                "RSI14": round(float(latest["RSI14"]), 2),
                "WATCH": bool(latest["WATCH"]),
                "RISK": bool(latest["RISK"]),
            }
        )

    summary_df = pd.DataFrame(summaries)
    summary_path = OUTPUT_DIR / "summary.csv"
    summary_df.to_csv(summary_path, index=False)
    return summary_df


if __name__ == "__main__":
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    result = run()
    print(result.to_string(index=False))
