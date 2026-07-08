#!/usr/bin/env python3
"""Module that slices specific columns and every 60th row of a DataFrame."""


def slice(df):
    """Extract specific columns and select every 60th row.

    Args:
        df (pandas.DataFrame): DataFrame containing High, Low,
        Close, and Volume_(BTC) columns.

    Returns:
        pandas.DataFrame: The sliced DataFrame.
    """
    df = df[['High', 'Low', 'Close', 'Volume_(BTC)']]
    df = df[::60]
    return df
