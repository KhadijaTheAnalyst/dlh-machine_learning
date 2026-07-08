#!/usr/bin/env python3
"""Module that computes descriptive statistics for a DataFrame."""


def analyze(df):
    """Compute descriptive statistics for all columns except Timestamp.

    Args:
        df (pandas.DataFrame): DataFrame to analyze.

    Returns:
        pandas.DataFrame: A new DataFrame containing the descriptive
        statistics.
    """
    df = df.drop(columns=['Timestamp'])
    stats = df.describe()
    return stats
