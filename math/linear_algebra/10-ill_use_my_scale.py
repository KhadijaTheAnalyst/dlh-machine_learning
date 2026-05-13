#!/usr/bin/env python3
"""
This module provides a function to get the shape of a numpy array.

The module includes:
- np_shape: Returns the shape of a numpy array

Author: KMustafa
Date: May 2026
"""


def np_shape(matrix):
    """
    Calculate the shape of a numpy array.

    Returns the dimensions of a numpy ndarray as a tuple of integers.
    The shape represents the size of the array in each dimension.

    Args:
        matrix (numpy.ndarray): A numpy array of any dimension

    Returns:
        tuple: The shape of the array as a tuple of integers

    Example:
        >>> mat1 = np.array([1, 2, 3, 4, 5, 6])
        >>> np_shape(mat1)
        (6,)

        >>> mat2 = np.array([])
        >>> np_shape(mat2)
        (0,)

        >>> mat3 = np.array([[[1, 2, 3], [4, 5, 6]]])
        >>> np_shape(mat3)
        (1, 2, 3)

    Note:
        - Works with arrays of any dimension (1D, 2D, 3D, etc.)
        - Returns a tuple, even fur 1D arrays (e.g., (6,) not 6)
        - No loops or conditional statements needed
        - No imports required
    """

    # The matrix parameter is already a numpy array
    # Access the .shape property which returns a tuple of dimensions
    # For example: (6,) for 1D, (2, 3) for 2D, (2, 2, 5) for 3D
    return matrix.shape
