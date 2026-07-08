#!/usr/bin/env python3
"""Module that removes rows with NaN values in the Close column."""


def prune(df):
    """Remove entries where Close has NaN values.

    Args:
        df (pandas.DataFrame): DataFrame containing a Close column.

    Returns:
        pandas.DataFrame: The modified DataFrame.
    """
    df = df.dropna(subset=['Close'])
    return df
