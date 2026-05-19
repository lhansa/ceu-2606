from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def load_monitoring_data(path: Path) -> pd.DataFrame:
    """Read monitoring data from a local Excel file."""
    return pd.read_excel(path)


def plot_time_series(data: pd.DataFrame, date_col: str, value_col: str) -> None:
    """Create a basic time-series line plot."""
    ordered = data.copy()
    ordered[date_col] = pd.to_datetime(ordered[date_col])
    ordered = ordered.sort_values(date_col)

    plt.figure(figsize=(10, 4))
    plt.plot(ordered[date_col], ordered[value_col])
    plt.title("Monitoring time series")
    plt.xlabel(date_col)
    plt.ylabel(value_col)
