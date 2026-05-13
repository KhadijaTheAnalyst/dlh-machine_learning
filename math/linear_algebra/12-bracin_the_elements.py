#!/usr/bin/env python3
"""
This module provides a function to perform element-wise operations on numpy arrays.

The module includes:
- np_elementwise: Performs element-wise addition, subtraction, multiplication, and division

Element-wise operations apply the same operation to each corresponding pair of elements
in two arrays, resulting in a new array with the same shape.

Author: KMustafa
Date: May 2026
"""

import numpy as np


def np_elementwise(mat1, mat2):
    """
    Perform element-wise addition, subtraction, multiplication, and division.
    
    Takes two numpy arrays and performs four element-wise operations:
    - Addition: adds corresponding elements
    - Subtraction: subtracts corresponding elements
    - Multiplication: multiplies corresponding elements
    - Division: divides corresponding elements
    
    Returns a tuple containing all four results.
    
    Args:
        mat1 (numpy.ndarray): First numpy array of any dimension
        mat2 (numpy.ndarray): Second numpy array of any dimension
                             Can be another array or a scalar number
    
    Returns:
        tuple: A tuple of four numpy arrays in this order:
               (sum, difference, product, quotient)
               where:
               - sum = mat1 + mat2 (element-wise addition)
               - difference = mat1 - mat2 (element-wise subtraction)
               - product = mat1 * mat2 (element-wise multiplication)
               - quotient = mat1 / mat2 (element-wise division)
    
    Example:
        >>> import numpy as np
        >>> mat1 = np.array([[11, 22, 33], [44, 55, 66]])
        >>> mat2 = np.array([[1, 2, 3], [4, 5, 6]])
        
        >>> add, sub, mul, div = np_elementwise(mat1, mat2)
        
        >>> add
        array([[12, 24, 36],
               [48, 60, 72]])
        
        >>> sub
        array([[10, 20, 30],
               [40, 50, 60]])
        
        >>> mul
        array([[ 11,  44,  99],
               [176, 275, 396]])
        
        >>> div
        array([[11., 11., 11.],
               [11., 11., 11.]])
        
        >>> # Works with scalars too
        >>> add, sub, mul, div = np_elementwise(mat1, 2)
        >>> add
        array([[13, 24, 35],
               [46, 57, 68]])
    
    Note:
        - Works with arrays of any dimension (1D, 2D, 3D, etc.)
        - Can perform operations with arrays or scalar numbers
        - Uses NumPy's built-in operators (no loops needed)
        - Results preserve the original array shape
        - Returns a tuple, always in this order: (add, sub, mul, div)
    """
    
    # Perform element-wise addition
    # mat1 + mat2: Adds each element of mat1 with corresponding element of mat2
    # NumPy automatically broadcasts to same shape if needed
    # Example: [[1, 2], [3, 4]] + 2 = [[3, 4], [5, 6]]
    add = mat1 + mat2
    
    # Perform element-wise subtraction
    # mat1 - mat2: Subtracts each element of mat2 from corresponding element of mat1
    # Example: [[11, 22], [33, 44]] - [[1, 2], [3, 4]] = [[10, 20], [30, 40]]
    sub = mat1 - mat2
    
    # Perform element-wise multiplication
    # mat1 * mat2: Multiplies each element of mat1 with corresponding element of mat2
    # Note: This is NOT matrix multiplication, just element-wise
    # Example: [[1, 2], [3, 4]] * [[5, 6], [7, 8]] = [[5, 12], [21, 32]]
    mul = mat1 * mat2
    
    # Perform element-wise division
    # mat1 / mat2: Divides each element of mat1 by corresponding element of mat2
    # Result is float type, even if inputs are integers
    # Example: [[11, 22], [33, 44]] / 2 = [[5.5, 11], [16.5, 22]]
    div = mat1 / mat2
    
    # Return all four results as a tuple in order: (add, sub, mul, div)
    # User can unpack like: add, sub, mul, div = np_elementwise(mat1, mat2)
    return (add, sub, mul, div)
