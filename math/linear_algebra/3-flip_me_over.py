#!/usr/bin/env python3
"""
This module provides functions for basic linear algebra
operations on 2D matrices.

The module includes:
- matrix_transpose: Returns the transpose of a 2D matrix

All functions assume matrices are non-empty and rectangular (all rows have
the same number of columns).

Author: KMustafa
Date: May 2026
"""


def matrix_transpose(matrix):
    """
    Returns the transpose of a 2D matrix.

    The transpose of a matrix is obtained by swapping rows and columns.
    Each column becomes a row, and each row becomes a column.

    Args:
        matrix (list of lists): A 2D matrix where each element is a list
                               representing a row. All rows have the same
                               number of columns.

    Returns:
        list of lists: A new transposed matrix where rows and
        columns are swapped.
                      Original matrix is not modified.

    Raises:
        IndexError: If matrix is empty.

    Example:
        >>> mat1 = [[1, 2], [3, 4]]
        >>> matrix_transpose(mat1)
        [[1, 3], [2, 4]]

        >>> mat2 = [[1, 2, 3], [4, 5, 6]]
        >>> matrix_transpose(mat2)
        [[1, 4], [2, 5], [3, 6]]

    Note:
        - Assumes all rows have the same length
        - Creates a new matrix (does not modify the original)
    """

    transpose_matrix = []
    # Outer loop: for each column
    for col_index in range(len(matrix[0])):
        new_row = []

    # Inner loop: for each row
        for row in matrix:
            new_row.append(row[col_index])

        transpose_matrix.append(new_row)
    return transpose_matrix
