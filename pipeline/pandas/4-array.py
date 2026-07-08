#!/usr/bin/env python3
"""Module that converts the last 10 rows of a DataFrame to a numpy array."""


def array(df):
    """Select the last 10 rows of High and Close and convert to ndarray.

    Args:
        df (pandas.DataFrame): DataFrame containing High and Close
        columns.

    Returns:
        numpy.ndarray: The selected values as a numpy array.
    """
    A = df[['High', 'Close']].tail(10).to_numpy()
    return A
