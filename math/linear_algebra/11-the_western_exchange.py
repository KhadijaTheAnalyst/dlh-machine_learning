#!/usr/bin/env python3
"""
This module provides a function to transpose a numpy array.

The module includes:
- np_transpose: Transposes a numpy array using the .T attribute

Transpose swaps rows and columns (or reverses all axes for multi-dimensional arrays).

Author: KMustafa
Date: May 2026
"""


def np_transpose(matrix):
    """
    Transpose a numpy array.

    Returns a new numpy array that is the transpose of the input matrix.
    The transpose operation swaps rows and columns for 2D arrays, and
    reverses all axes for multi-dimensional arrays.

    Args:
        matrix (numpy.ndarray): A numpy array of any dimension

    Returns:
        numpy.ndarray: A new transposed numpy array

    Example:
        >>> import numpy as np
        >>> mat = np.array([[1, 2, 3], [4, 5, 6]])
        >>> np_transpose(mat)
        array([[1, 4],
               [2, 5],
               [3, 6]])

        >>> mat1d = np.array([1, 2, 3, 4, 5, 6])
        >>> np_transpose(mat1d)
        array([1, 2, 3, 4, 5, 6])

    Note:
        - For 1D arrays, the result is the same as the input
        - For 2D arrays, rows become columns and columns become rows
        - For 3D+ arrays, all axes are reversed
        - Uses the .T attribute of numpy arrays (no loops needed)
        - No imports required (assumes input is already numpy array)
    """

    # Access the .T property of the numpy array
    # The .T attribute returns a transposed view of the array
    # It works for any number of dimensions
    #
    # Examples:
    # 2D array: [[1, 2], [3, 4]] → [[1, 3], [2, 4]]
    # 1D array: [1, 2, 3] → [1, 2, 3] (unchanged)
    # 3D array: All axes are reversed
    return matrix.T
