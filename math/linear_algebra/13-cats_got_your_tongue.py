#!/usr/bin/env python3
"""
This module provides a function to concatenate two numpy arrays along a specific axis.

The module includes:
- np_cat: Concatenates two numpy arrays along a specified axis (0 or 1)

Concatenation combines two arrays either vertically (axis=0) or horizontally (axis=1).

Author: KMustafa
Date: May 2026
"""

import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    Concatenate two numpy arrays along a specific axis.
    
    Joins two numpy arrays either vertically (by rows) or horizontally (by columns)
    depending on the axis parameter. Returns a new array without modifying the
    original arrays.
    
    Args:
        mat1 (numpy.ndarray): First numpy array of any dimension
        mat2 (numpy.ndarray): Second numpy array of any dimension
        axis (int, optional): Direction of concatenation. Defaults to 0.
                             - axis=0: Concatenate vertically (stack rows)
                               Requirement: Both arrays must have same columns
                             - axis=1: Concatenate horizontally (stack columns)
                               Requirement: Both arrays must have same rows
    
    Returns:
        numpy.ndarray: A new concatenated numpy array if shapes match.
                      Returns None if arrays cannot be concatenated.
    
    Example:
        >>> import numpy as np
        >>> mat1 = np.array([[1, 2], [3, 4]])
        >>> mat2 = np.array([[5, 6], [7, 8]])
        
        >>> # Concatenate vertically (axis=0)
        >>> np_cat(mat1, mat2, axis=0)
        array([[1, 2],
               [3, 4],
               [5, 6],
               [7, 8]])
        
        >>> # Concatenate horizontally (axis=1)
        >>> np_cat(mat1, mat2, axis=1)
        array([[1, 2, 5, 6],
               [3, 4, 7, 8]])
    
    Note:
        - For axis=0: Both arrays must have the same number of columns
        - For axis=1: Both arrays must have the same number of rows
        - Returns a new array (does not modify original arrays)
        - axis=0 is the default parameter
        - Uses NumPy's concatenate function (no loops needed)
    """
    
    # Use numpy's concatenate function to join the arrays
    # np.concatenate() takes a tuple of arrays to concatenate
    # The axis parameter specifies the direction:
    #   - axis=0: Stack vertically (add rows)
    #   - axis=1: Stack horizontally (add columns)
    #
    # Example:
    # mat1 = [[1, 2],      mat2 = [[5, 6],
    #         [3, 4]]              [7, 8]]
    #
    # axis=0: [[1, 2],            axis=1: [[1, 2, 5, 6],
    #          [3, 4],                     [3, 4, 7, 8]]
    #          [5, 6],
    #          [7, 8]]
    
    return np.concatenate((mat1, mat2), axis=axis)
