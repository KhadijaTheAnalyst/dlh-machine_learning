#!/usr/bin/env python3
"""Module that creates a pandas DataFrame from a np.ndarray."""
import pandas as pd


def from_numpy(array):
    """Create a pandas DataFrame from a np.ndarray.

    Args:
        array (numpy.ndarray): The array to convert.

    Returns:
        pandas.DataFrame: A new DataFrame with default column
        labels (A, B, C, ...) generated automatically.
    """
    df = pd.DataFrame(array)
    return df
