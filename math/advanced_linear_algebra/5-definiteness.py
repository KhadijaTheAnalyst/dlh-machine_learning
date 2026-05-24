#!/usr/bin/env python3
"""
Matrix Definiteness Module

This module provides functionality to determine the definiteness of a square
matrix by analyzing its eigenvalues.
"""

import numpy as np


def definiteness(matrix):
    """
    Determines the definiteness of an n×n square matrix.

    The definiteness is calculated by computing all eigenvalues of the matrix
    and analyzing their signs. A matrix must be square and non-empty to have
    a definable definiteness.
    """

    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    if matrix.ndim != 2:
        return None

    rows, cols = matrix.shape
    if rows == 0 or cols == 0:
        return None

    if rows != cols:
        return None
    
    if not np.allclose(matrix, matrix.T):
        return None

    eigenvalues = np.linalg.eigvals(matrix)

    all_positive = all(eig > 0 for eig in eigenvalues)
    all_negative = all(eig < 0 for eig in eigenvalues)
    all_non_negative = all(eig >= 0 for eig in eigenvalues)
    all_non_positive = all(eig <= 0 for eig in eigenvalues)

    if all_positive:
        return "Positive definite"
    elif all_negative:
        return "Negative definite"
    elif all_non_negative:
        return "Positive semi-definite"
    elif all_non_positive:
        return "Negative semi-definite"
    else:
        return "Indefinite"
