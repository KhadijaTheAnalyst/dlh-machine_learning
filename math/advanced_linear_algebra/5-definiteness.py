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

    """
    # ========== INPUT VALIDATION SECTION ==========

    # Validate that input is a numpy array (type check)
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    # Validate that the array is 2D (not 1D or higher dimensional)
    if matrix.ndim != 2:
        return None

    # Extract matrix dimensions for validation
    rows, cols = matrix.shape

    # Check if matrix is empty (0 rows or 0 columns)
    if rows == 0 or cols == 0:
        return None

    # Check if matrix is square (required for eigenvalue-based definiteness)
    if rows != cols:
        return None

    # Symmetry check
    if not np.allclose(matrix, matrix.T):
        return None

    # ========== EIGENVALUE COMPUTATION ==========

    # Compute all eigenvalues of the matrix
    # np.linalg.eigvals returns an array of eigenvalues
    eigenvalues = np.linalg.eigvals(matrix)

    # ========== DEFINITENESS CLASSIFICATION ==========

    # Check if ALL eigenvalues are positive (> 0)
    all_positive = all(eig > 0 for eig in eigenvalues)

    # Check if ALL eigenvalues are negative (< 0)
    all_negative = all(eig < 0 for eig in eigenvalues)

    # Check if ALL eigenvalues are non-negative (≥ 0)
    # This includes positive and zero eigenvalues
    all_non_negative = all(eig >= 0 for eig in eigenvalues)

    # Check if ALL eigenvalues are non-positive (≤ 0)
    # This includes negative and zero eigenvalues
    all_non_positive = all(eig <= 0 for eig in eigenvalues)

    # ========== RETURN APPROPRIATE CLASSIFICATION ==========

    # Order matters: check strictly positive/negative first, then semi-definite
    if all_positive:
        return "Positive definite"
    elif all_negative:
        return "Negative definite"
    elif all_non_negative:
        # At this point we know not all are positive (checked above)
        # So at least one must be 0
        return "Positive semi-definite"
    elif all_non_positive:
        # At this point we know not all are negative (checked above)
        # So at least one must be 0
        return "Negative semi-definite"
    else:
        # If none of the above, eigenvalues have mixed signs
        return "Indefinite"
