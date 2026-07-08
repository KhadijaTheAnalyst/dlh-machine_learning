#!/usr/bin/env python3
"""Module that sets the Timestamp column as the DataFrame index."""


def index(df):
    """Set the Timestamp column as the index of the DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame containing a Timestamp
        column.

    Returns:
        pandas.DataFrame: The modified DataFrame.
    """
    df = df.set_index('Timestamp')
    return df
