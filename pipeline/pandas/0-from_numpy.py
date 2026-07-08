#!/usr/bin/env python3
"""Module that creates a pandas DataFrame from a np.ndarray."""
import pandas as pd


def from_numpy(array):
    """Create a pandas DataFrame from a np.ndarray.

    Args:
        array (numpy.ndarray): The array to convert.

    Returns:
        pandas.DataFrame: A new DataFrame with columns labeled
        alphabetically (A, B, C, ...) based on the number of
        columns in array.
    """
    columns = list(string.ascii_uppercase[:array.shape[1]])
    df = pd.DataFrame(array, columns=columns)
    return df
