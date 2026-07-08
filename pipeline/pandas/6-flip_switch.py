#!/usr/bin/env python3
"""Module that reverses and transposes a DataFrame."""


def flip_switch(df):
    """Sort a DataFrame in reverse chronological order and transpose it.

    Args:
        df (pandas.DataFrame): DataFrame to transform.

    Returns:
        pandas.DataFrame: The reverse-sorted, transposed DataFrame.
    """
    df = df.sort_index(ascending=False)
    df = df.transpose()
    return df
