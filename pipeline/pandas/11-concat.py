#!/usr/bin/env python3
"""Module that concatenates two DataFrames indexed on Timestamp."""
import pandas as pd
index = __import__('10-index').index


def concat(df1, df2):
    """Index df1 and df2 on Timestamp and concatenate them.

    Args:
        df1 (pandas.DataFrame): The coinbase DataFrame.
        df2 (pandas.DataFrame): The bitstamp DataFrame.

    Returns:
        pandas.DataFrame: The concatenated DataFrame, with df2 rows
        (up to and including timestamp 1417411920) on top of df1,
        labeled with keys 'bitstamp' and 'coinbase'.
    """
    df1 = index(df1)
    df2 = index(df2)
    df2 = df2[df2.index <= 1417411920]
    df = pd.concat([df2, df1], keys=['bitstamp', 'coinbase'])
    return df
