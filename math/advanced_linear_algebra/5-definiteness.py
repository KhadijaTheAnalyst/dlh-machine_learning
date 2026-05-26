#!/usr/bin/env python3
"""
Matrix Definiteness Module
 
This module provides functionality to determine the definiteness of a square
matrix by analyzing its eigenvalues.
 
A square matrix's definiteness describes the sign characteristics of all its
eigenvalues and is crucial in optimization, linear algebra, and numerical
analysis.
 
The definiteness classification is:
    - Positive Definite: All eigenvalues > 0
    - Positive Semi-Definite: All eigenvalues ≥ 0 (at least one = 0)
    - Negative Definite: All eigenvalues < 0
    - Negative Semi-Definite: All eigenvalues ≤ 0 (at least one = 0)
    - Indefinite: Mixed sign eigenvalues (some positive, some negative)
 
Applications:
    - Optimization: Positive definite Hessian indicates a minimum
    - Statistics: Covariance matrices are positive semi-definite
    - Numerical Analysis: Determines matrix properties for solving systems
 
Functions:
    definiteness(matrix): Determines the definiteness classification of a matrix.
 
Dependencies:
    - numpy: For eigenvalue computation and array operations
 
Example:
    >>> import numpy as np
    >>> definiteness = __import__('5-definiteness').definiteness
    >>> mat = np.array([[4, 1], [1, 3]])
    >>> definiteness(mat)
    'Positive definite'
"""

import numpy as np


def definiteness(matrix):
    """
    Determines the definiteness of an n×n square matrix.
 
    The definiteness is calculated by computing all eigenvalues of the matrix
    and analyzing their signs. A matrix must be square and non-empty to have
    a definable definiteness.
 
    Parameters:
        matrix (numpy.ndarray): A square n×n numpy array whose definiteness
                               is to be determined. Must be 2D and have equal
                               number of rows and columns.
 
    Returns:
        str: One of the following strings describing the definiteness:
            - "Positive definite": All eigenvalues > 0
            - "Negative definite": All eigenvalues < 0
            - "Positive semi-definite": All eigenvalues ≥ 0 (at least one = 0)
            - "Negative semi-definite": All eigenvalues ≤ 0 (at least one = 0)
            - "Indefinite": Eigenvalues have mixed signs
 
        Returns None if:
            - The matrix is not 2D
            - The matrix is empty (0 rows or 0 columns)
            - The matrix is not square (rows ≠ columns)
            - The matrix doesn't fit any definiteness category
 
    Raises:
        TypeError: If matrix is not a numpy.ndarray. Raises with message:
                  "matrix must be a numpy.ndarray"
 
    Example:
        >>> mat1 = np.array([[4, 1], [1, 3]])
        >>> definiteness(mat1)
        'Positive definite'
 
        >>> mat2 = np.array([[2, 4], [4, 8]])
        >>> definiteness(mat2)
        'Positive semi-definite'
 
        >>> mat3 = np.array([[-1, 1], [1, -1]])
        >>> definiteness(mat3)
        'Indefinite'
 
        >>> mat4 = np.array([[1, 2, 3], [4, 5, 6]])
        >>> definiteness(mat4)  # Non-square
        None
 
    Note:
        - Only square matrices (n×n) can have a defined definiteness
        - The matrix must be a numpy.ndarray, not a Python list
        - Eigenvalues are computed numerically and may have floating-point errors
        - For symmetric/Hermitian matrices, definiteness is most meaningful
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
