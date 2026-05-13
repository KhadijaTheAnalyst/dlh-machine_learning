#!/usr/bin/env python3
"""
This module provides a function to perform matrix multiplication on numpy arrays.

The module includes:
- np_matmul: Performs matrix multiplication on two numpy arrays

Matrix multiplication combines rows from the first matrix with columns from the
second matrix using the dot product operation.

Author: KMustafa
Date: May 2026
"""

import numpy as np


def np_matmul(mat1, mat2):
    """
    Perform matrix multiplication on two numpy arrays.
    
    Multiplies two matrices using the standard matrix multiplication algorithm.
    Each element in the result is calculated by taking the dot product of a row
    from mat1 and a column from mat2.
    
    This is different from element-wise multiplication (*).
    Matrix multiplication uses the @ operator or np.matmul().
    
    Args:
        mat1 (numpy.ndarray): First numpy array
                             Shape: (m, n) where m = rows, n = columns
        mat2 (numpy.ndarray): Second numpy array
                             Shape: (n, p) where n = rows, p = columns
    
    Returns:
        numpy.ndarray: A new numpy array representing the matrix product
                      Shape: (m, p) - number of rows from mat1, columns from mat2
    
    Requirements:
        - Number of COLUMNS in mat1 must equal number of ROWS in mat2
        - mat1 shape (m, n) and mat2 shape (n, p) → Result shape (m, p)
    
    How It Works:
        Result[i][j] = (Row i of mat1) · (Column j of mat2)
        
        The dot product is calculated as:
        Row [a, b, c] · Column [x, y, z] = (a*x) + (b*y) + (c*z)
    
    Example:
        >>> import numpy as np
        >>> mat1 = np.array([[11, 22, 33], [44, 55, 66]])
        >>> mat2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        
        >>> np_matmul(mat1, mat2)
        array([[ 330,  396,  462],
               [ 726,  891, 1056]])
        
        >>> # Another example with column vector
        >>> mat3 = np.array([[7], [8], [9]])
        >>> np_matmul(mat1, mat3)
        array([[ 550],
               [1342]])
    
    Calculation Details (First Example):
        mat1 shape: 2×3 (2 rows, 3 columns)
        mat2 shape: 3×3 (3 rows, 3 columns)
        Result shape: 2×3 (2 rows, 3 columns)
        
        Result[0][0] = 11*1 + 22*4 + 33*7 = 11 + 88 + 231 = 330
        Result[0][1] = 11*2 + 22*5 + 33*8 = 22 + 110 + 264 = 396
        Result[1][0] = 44*1 + 55*4 + 66*7 = 44 + 220 + 462 = 726
        
        So result = [[330, 396, 462], [726, 891, 1056]]
    
    Note:
        - Uses numpy's matmul function (no loops needed)
        - Different from element-wise multiplication (*)
        - Matrix multiplication is NOT commutative: A·B ≠ B·A
        - Works with arrays of 2D or higher
    """
    
    # Use numpy's matmul function to perform matrix multiplication
    # np.matmul(mat1, mat2) computes the matrix product
    #
    # Alternatively, you can use the @ operator:
    # return mat1 @ mat2
    #
    # Both are equivalent:
    # np.matmul(mat1, mat2) == mat1 @ mat2
    #
    # How it differs from element-wise multiplication:
    # Element-wise: mat1 * mat2 → [1, 2] * [3, 4] = [3, 8]
    # Matrix mult: mat1 @ mat2 → [1, 2] @ [3, 4]^T = 1*3 + 2*4 = 11
    #
    # Example calculation:
    # mat1 = [[1, 2, 3],      mat2 = [[1, 2],
    #         [4, 5, 6]]              [3, 4],
    #                                 [5, 6]]
    #
    # Result[0][0] = 1*1 + 2*3 + 3*5 = 1 + 6 + 15 = 22
    # Result[0][1] = 1*2 + 2*4 + 3*6 = 2 + 8 + 18 = 28
    # Result[1][0] = 4*1 + 5*3 + 6*5 = 4 + 15 + 30 = 49
    # Result[1][1] = 4*2 + 5*4 + 6*6 = 8 + 20 + 36 = 64
    #
    # Result = [[22, 28], [49, 64]]

    return np.matmul(mat1, mat2)
