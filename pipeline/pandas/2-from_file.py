#!/usr/bin/env python3
"""Module that loads data from a file into a pandas DataFrame."""
import pandas as pd


def from_file(filename, delimiter):
    """Load data from a file as a pd.DataFrame.

    Args:
        filename (str): The file to load from.
        delimiter (str): The column separator.

    Returns:
        pandas.DataFrame: The loaded DataFrame.
    """
    df = pd.read_csv(filename, delimiter=delimiter)
    return df
