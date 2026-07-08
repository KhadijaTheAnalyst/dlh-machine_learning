#!/usr/bin/env python3
"""Module that cleans and fills missing values in a DataFrame."""


def fill(df):
    """Drop Weighted_Price and fill missing values in other columns.

    Args:
        df (pandas.DataFrame): DataFrame to clean.

    Returns:
        pandas.DataFrame: The modified DataFrame.
    """
    df = df.drop(columns=['Weighted_Price'])
    df['Close'] = df['Close'].ffill()
    df['High'] = df['High'].fillna(df['Close'])
    df['Low'] = df['Low'].fillna(df['Close'])
    df['Open'] = df['Open'].fillna(df['Close'])
    df['Volume_(BTC)'] = df['Volume_(BTC)'].fillna(0)
    df['Volume_(Currency)'] = df['Volume_(Currency)'].fillna(0)
    return df
