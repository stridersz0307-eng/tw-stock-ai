# tw-stock-ai

A lightweight Python + pandas MVP that computes technical indicators and simple risk/watch signals for a Taiwan stock list.

## Project structure

- `app/data_loader.py`: Loads stock symbols and generates sample close-price data.
- `app/indicators.py`: Computes MA5/MA20/MA60 and RSI(14).
- `app/signals.py`: Generates `WATCH` and `RISK` signals.
- `app/run.py`: End-to-end entry point.
- `data/stock_list.csv`: Input stock symbols.
- `outputs/`: Generated output CSV files.

## Signals

- `WATCH`: `True` when `price > MA20`
- `RISK`: `True` when `price < MA60`

## Usage

```bash
python app/run.py
```

Outputs:
- `outputs/<stock_id>_signals.csv`
- `outputs/summary.csv`
