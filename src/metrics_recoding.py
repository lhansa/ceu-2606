import matplotlib.pyplot as plt
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage


def correlation_matrix(data: pd.DataFrame) -> pd.DataFrame:
    """Compute a correlation matrix for numeric columns."""
    return data.select_dtypes(include="number").corr()


def hierarchical_linkage(data: pd.DataFrame, method: str = "ward"):
    """Build hierarchical clustering linkage matrix for numeric columns."""
    numeric = data.select_dtypes(include="number").dropna()
    return linkage(numeric.T, method=method)


def plot_dendrogram(linkage_matrix, labels=None) -> None:
    """Plot a dendrogram for clustered metrics."""
    plt.figure(figsize=(10, 5))
    dendrogram(linkage_matrix, labels=labels)
    plt.title("Metrics dendrogram")
    plt.xlabel("Metric")
    plt.ylabel("Distance")
