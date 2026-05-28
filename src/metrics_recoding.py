import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from numpy.typing import NDArray
from scipy.cluster.hierarchy import dendrogram, linkage


def correlation_matrix(data: pd.DataFrame) -> pd.DataFrame:
    """Compute a correlation matrix for numeric columns."""
    return data.select_dtypes(include="number").corr()


def hierarchical_linkage(data: pd.DataFrame, method: str = "ward") -> NDArray[np.float64]:
    """Build hierarchical clustering linkage matrix for numeric columns."""
    numeric = data.select_dtypes(include="number").dropna()
    return linkage(numeric.T, method=method)


def plot_dendrogram(
    linkage_matrix: NDArray[np.float64], labels: list[str] | None = None
) -> tuple[Figure, Axes]:
    """Plot a dendrogram for clustered metrics."""
    fig, ax = plt.subplots(figsize=(10, 5))
    dendrogram(linkage_matrix, labels=labels, ax=ax, orientation="left")
    ax.set_title("Metrics dendrogram")
    ax.set_xlabel("Metric")
    ax.set_ylabel("Distance")
    fig.tight_layout()
    return fig, ax
