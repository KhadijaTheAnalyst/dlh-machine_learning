#!/usr/bin/env python3
"""
Matrix Adjugate Module

This module provides functionality to compute
the adjugate (also known as adjoint)
matrix of an n×n square matrix. The adjugate matrix
is a fundamental concept in
linear algebra, primarily used in computing the
inverse of a matrix.

The adjugate of a matrix A is the transpose of its cofactor matrix.
Mathematically:
    adj(A) = cofactor(A)^T (transpose of the cofactor matrix)

The adjugate matrix has a key property related to matrix inversion:
    A * adj(A) = adj(A) * A = det(A) * I

Where det(A) is the determinant of A, and I is the identity matrix.

This relationship is used to compute the inverse of a matrix:
    A^(-1) = (1/det(A)) * adj(A)  (when det(A) ≠ 0)

Functions:
    adjugate(matrix): Computes the adjugate matrix of an n×n matrix.

Dependencies:
    - Requires the '2-cofactor' module for cofactor and
    determinant calculations.

Example:
    >>> adjugate = __import__('3-adjugate').adjugate
    >>> mat = [[1, 2], [3, 4]]
    >>> result = adjugate(mat)
    >>> result
    [[4, -2], [-3, 1]]
"""

determinant = __import__('2-cofactor').determinant
cofactor = __import__('2-cofactor').cofactor


def adjugate(matrix):
    """
    Computes the adjugate (adjoint) matrix of an n×n square matrix.

    The adjugate matrix is obtained by computing the cofactor matrix and then
    transposing it. It is used in the calculation of a matrix's inverse.

    For an n×n matrix A, if adj(A) is its adjugate matrix, then:
        A * adj(A) = adj(A) * A = det(A) * I

    Where det(A) is the determinant of A and I is the n×n identity matrix.

    Parameters:
        matrix (list of lists):
        A square n×n matrix where each element is a
        list representing a row. All rows must have the
        same number of columns, and the number of rows
        must equal the number of columns (n×n requirement).

    Returns:
        list of lists:
        A new matrix of the same size as the input, containing
        the adjugate matrix (transpose of the cofactor matrix).
        The original input matrix is not modified.

    Raises:
        IndexError: If the matrix is empty or has inconsistent row lengths.
        ValueError: If the matrix is not square (rows ≠ columns).

    Example:
        >>> adjugate([[5]])
        [[1]]

        >>> adjugate([[1, 2], [3, 4]])
        [[4, -2], [-3, 1]]

        >>> adjugate([[1, 1], [1, 1]])
        [[1, 1], [1, 1]]

        >>> adjugate([[5, 7, 9], [3, 1, 8], [6, 2, 4]])
        [[-20, 50, 55], [40, -26, -58], [-9, -28, -16]]

    Note:
        - The input matrix must be square (n×n). Non-square matrices will raise
          a ValueError.
        - For a 1×1 matrix [[a]], the adjugate is [[1]] (the cofactor is 1).
        - The adjugate matrix is particularly useful for computing the inverse:
          If det(A) ≠ 0, then A^(-1) = (1/det(A)) * adj(A).
        - This function depends on the cofactor function from module
        '2-cofactor'.
    """
    c = cofactor(matrix)  # Get the cofactor matrix

    # Transpose the cofactor matrix to compute the adjugate
    transpose_matrix = []
    for col_index in range(len(c[0])):
        new_row = []
        for row in c:
            new_row.append(row[col_index])
        transpose_matrix.append(new_row)

    return transpose_matrix
