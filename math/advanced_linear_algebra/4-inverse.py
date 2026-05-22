#!/usr/bin/env python3
"""
Matrix Inverse Module

This module provides functionality to compute the
inverse of an n×n square matrix
using the adjugate matrix and determinant.

The inverse of a matrix A is the matrix A⁻¹ such that:
    A * A⁻¹ = A⁻¹ * A = I

Where I is the n×n identity matrix.

A matrix has an inverse if and only if its determinantis
non-zero (non-singular).

The inverse is computed using the formula:
    A⁻¹ = (1/det(A)) * adj(A)

Where det(A) is the determinant of A and adj(A) is the adjugate matrix.

Functions:
    inverse(matrix): Computes the inverse of an n×n square matrix.

Dependencies:
    - Requires the '3-adjugate' module for adjugate matrix calculation.
    - Requires the '0-determinant' module for determinant calculation.

Example:
    >>> inverse = __import__('4-inverse').inverse
    >>> mat = [[1, 2], [3, 4]]
    >>> result = inverse(mat)
    >>> result
    [[-2.0, 1.0], [1.5, -0.5]]
"""

adjugate = __import__("3-adjugate").adjugate
determinant = __import__("0-determinant").determinant


def inverse(matrix):
    """
    Computes the inverse of an n×n square matrix.

    The inverse of a matrix A is the matrix A⁻¹ such that:
        A * A⁻¹ = A⁻¹ * A = I

    Where I is the identity matrix. The inverse is computed using the formula:
        A⁻¹ = (1/det(A)) * adj(A)

    A matrix only has an inverse if its determinant is non-zero. A matrix with
    a zero determinant is called singular or non-invertible.

    Parameters:
        matrix (list of lists): A square n×n matrix where each element is a
                               list representing a row. All rows must have the
                               same number of columns, and the number of rows
                               must equal the number of columns
                               (n×n requirement).

    Returns:
        list of lists: A new n×n matrix containing the inverse of the input
                      matrix. Each element is a float representing the scaled
                      adjugate matrix element (adjugate[i][j] / det(matrix)).

                      Returns None if the matrix is singular
                      (determinant == 0),
                      indicating no inverse exists.

                      The original input matrix is not modified.

    Raises:
        IndexError: If the matrix is empty or has inconsistent row lengths.
        ValueError: If the matrix is not square (rows ≠ columns).
        ZeroDivisionError: Should not occur (caught by determinant == 0 check).

    Example:
        >>> inverse([[5]])
        [[0.2]]

        >>> inverse([[1, 2], [3, 4]])
        [[-2.0, 1.0], [1.5, -0.5]]

        >>> inverse([[1, 1], [1, 1]])
        None

        >>> inverse([[5, 7, 9], [3, 1, 8], [6, 2, 4]])
        [[0.0196..., -0.0490..., 0.0540...], ...]

    Note:
        - The input matrix must be square (n×n). Non-square matrices will raise
          a ValueError.
        - A singular matrix (determinant = 0) has no inverse. The function
          returns None in this case.
        - The inverse is particularly useful for solving systems of linear
          equations: If Ax = b, then x = A⁻¹ * b.
        - For numerical stability, this method works well for small matrices.
          For larger matrices, numerical methods like LU decomposition are
          preferred to avoid floating-point errors.
        - This function depends on the adjugate() and determinant() functions.
    """
    # Calculate the adjugate matrix
    adj = adjugate(matrix)

    # Get matrix dimension
    n = len(adj)

    # Calculate the determinant of the original matrix
    det = determinant(matrix)

    # Check if matrix is singular (non-invertible)
    if det == 0:
        return None

    # Build the inverse matrix: each element = adjugate[i][j] / det
    inverse_matrix = []
    for i in range(n):
        new_row = []
        for j in range(n):
            # Divide each adjugate element by the determinant
            inverse_element = adj[i][j] / det
            new_row.append(inverse_element)
        inverse_matrix.append(new_row)

    return inverse_matrix
