#!/usr/bin/env python3
"""Module that renames a DataFrame column and converts it to datetime."""
import pandas as pd


def rename(df):
    """Rename the Timestamp column to Datetime and convert its values.

    Args:
        df (pandas.DataFrame): DataFrame containing a Timestamp column.

    Returns:
        pandas.DataFrame: The modified DataFrame with only the
        Datetime and Close columns.
    """
    df = df.rename(columns={'Timestamp': 'Datetime'})
    df['Datetime'] = pd.to_datetime(df['Datetime'], unit='s')
    df = df[['Datetime', 'Close']]
    return df
