#!/usr/bin/env python3
"""Module that rearranges a MultiIndex to put Timestamp first."""
import pandas as pd
index = __import__('10-index').index


def hierarchy(df1, df2):
    """Concatenate df1 and df2 with Timestamp as the top MultiIndex level.

    Args:
        df1 (pandas.DataFrame): The coinbase DataFrame.
        df2 (pandas.DataFrame): The bitstamp DataFrame.

    Returns:
        pandas.DataFrame: The concatenated DataFrame, filtered to
        timestamps 1417411980 to 1417417980 inclusive, with
        Timestamp as the first MultiIndex level and rows in
        chronological order.
    """
    df1 = index(df1)
    df2 = index(df2)

    df1 = df1[(df1.index >= 1417411980) & (df1.index <= 1417417980)]
    df2 = df2[(df2.index >= 1417411980) & (df2.index <= 1417417980)]

    df = pd.concat([df2, df1], keys=['bitstamp', 'coinbase'])
    df = df.reorder_levels([1, 0])
    df = df.sort_index(level=0)
    return df
