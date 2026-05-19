from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.axes import Axes
from matplotlib.figure import Figure


def load_monitoring_data(path: Path) -> pd.DataFrame:
    """Read monitoring data from a local Excel file."""
    return pd.read_excel(path)


def plot_time_series(
    data: pd.DataFrame, date_col: str, value_col: str
) -> tuple[Figure, Axes]:
    """Create a basic time-series line plot."""
    ordered = data.copy()
    ordered[date_col] = pd.to_datetime(ordered[date_col])
    ordered = ordered.sort_values(date_col)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(ordered[date_col], ordered[value_col])
    ax.set_title("Monitoring time series")
    ax.set_xlabel(date_col)
    ax.set_ylabel(value_col)
    return fig, ax
