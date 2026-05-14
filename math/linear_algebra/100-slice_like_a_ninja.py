#!/usr/bin/env python3
"""
This module provides functions to slice numpy arrays along specific axes dynamically.

The module includes:
- np_slice: Main function that slices a matrix along specific axes (Method 1)
- np_slice_method2: Using tuple comprehension (Method 2)
- np_slice_method3: Using dictionary .get() method (Method 3)
- np_slice_method4: Using list comprehension (Method 4)

All methods handle variable tuple lengths (2 or 3 values: start, stop, or start, stop, step).

Author: KMustafa
Date: May 2026
"""

import numpy as np


def np_slice(matrix, axes={}):
    """
    Slice a matrix along specific axes using dynamic slicing.
    
    METHOD 1: Build slice list, update it, convert to tuple (Recommended for clarity).
    
    Slices a numpy array along specified axes without knowing which axes
    will be used ahead of time. Each axis can have a slice specification
    with 2 values (start, stop) or 3 values (start, stop, step).
    
    Args:
        matrix (numpy.ndarray): A numpy array of any dimension
        axes (dict, optional): Dictionary where:
                              - key: axis number (0, 1, 2, ...)
                              - value: tuple (start, stop) or (start, stop, step)
                              Defaults to empty dict (no slicing).
    
    Returns:
        numpy.ndarray: A new sliced numpy array
    
    Example:
        >>> import numpy as np
        >>> matrix = np.array([[[1, 2, 3], [4, 5, 6]],
        ...                    [[7, 8, 9], [10, 11, 12]]])
        
        >>> # Slice axis 0 (0:1) and axis 2 (1:3)
        >>> np_slice(matrix, {0: (0, 1), 2: (1, 3)})
        array([[[ 2,  3],
                [ 5,  6]]])
        
        >>> # Slice with step: axis 0 (1:3, step 1)
        >>> np_slice(matrix, {0: (1, 3, 1)})
        array([[[ 7,  8,  9],
                [10, 11, 12]]])
        
        >>> # No axes specified (return copy of entire matrix)
        >>> np_slice(matrix, {})
        array([[[ 1,  2,  3],
                [ 4,  5,  6]],
        
               [[ 7,  8,  9],
                [10, 11, 12]]])
    
    Note:
        - Axes not specified in dictionary will take all elements (slice(None))
        - Tuples can have 2 values (start, stop) or 3 (start, stop, step)
        - slice(*tuple) unpacks tuple into slice() parameters
        - No loops or conditionals needed (except for building slices)
    """
    
    # STEP 1: Create default slices for all dimensions
    # slice(None) is equivalent to : which means "take all elements in this dimension"
    # Example: For a 3D array, create [slice(None), slice(None), slice(None)]
    # This represents [:, :, :]
    slices = [slice(None)] * matrix.ndim
    
    # STEP 2: Update slices based on axes dictionary
    # For each axis specified in the dictionary, replace the slice
    for axis, slice_tuple in axes.items():
        # slice(*slice_tuple) unpacks the tuple into slice parameters
        # If slice_tuple = (1, 3), it becomes slice(1, 3) = 1:3
        # If slice_tuple = (1, 3, 1), it becomes slice(1, 3, 1) = 1:3:1
        slices[axis] = slice(*slice_tuple)
    
    # STEP 3: Convert list to tuple and apply to matrix
    # NumPy requires a tuple for multi-dimensional indexing
    # matrix[tuple(slices)] is equivalent to matrix[slices[0], slices[1], slices[2], ...]
    return matrix[tuple(slices)]


def np_slice_method2(matrix, axes={}):
    """
    METHOD 2: Using tuple comprehension (More Pythonic).
    
    Slice a matrix along specific axes using a tuple comprehension.
    This is more concise and Pythonic than Method 1.
    
    Args:
        matrix (numpy.ndarray): A numpy array of any dimension
        axes (dict, optional): Dictionary of axes to slice
    
    Returns:
        numpy.ndarray: A new sliced numpy array
    
    Example:
        >>> matrix = np.array([[[1, 2, 3], [4, 5, 6]],
        ...                    [[7, 8, 9], [10, 11, 12]]])
        >>> np_slice_method2(matrix, {0: (0, 1), 2: (1, 3)})
        array([[[ 2,  3],
                [ 5,  6]]])
    
    Note:
        - Uses tuple comprehension for cleaner code
        - Single-line slicing without intermediate list
        - More Pythonic approach
    """
    
    # Create tuple of slices using comprehension
    # For each dimension i from 0 to ndim:
    #   - If i is in axes: use slice(*axes[i]) to unpack the tuple
    #   - Otherwise: use slice(None) to take all elements
    # This builds the slices directly as a tuple
    slices = tuple(
        slice(*axes[i]) if i in axes else slice(None)
        for i in range(matrix.ndim)
    )
    
    # Apply the tuple of slices to the matrix
    return matrix[slices]


def np_slice_method3(matrix, axes={}):
    """
    METHOD 3: Using dictionary .get() method (Clean and Elegant).
    
    Slice a matrix using the dictionary .get() method to handle missing axes.
    This avoids the if-else check and is very elegant.
    
    Args:
        matrix (numpy.ndarray): A numpy array of any dimension
        axes (dict, optional): Dictionary of axes to slice
    
    Returns:
        numpy.ndarray: A new sliced numpy array
    
    Example:
        >>> matrix = np.array([[[1, 2, 3], [4, 5, 6]],
        ...                    [[7, 8, 9], [10, 11, 12]]])
        >>> np_slice_method3(matrix, {0: (0, 1), 2: (1, 3)})
        array([[[ 2,  3],
                [ 5,  6]]])
    
    Note:
        - Uses dict.get(key, default) to handle missing axes
        - (None, None) unpacks to slice(None, None) = slice(None)
        - Most elegant solution
    """
    
    # Create tuple of slices using .get() method
    # dict.get(i, default) returns:
    #   - axes[i] if i exists in axes
    #   - (None, None) if i doesn't exist
    # slice(None, None) is equivalent to slice(None) which is :
    slices = tuple(
        slice(*axes.get(i, (None, None)))
        for i in range(matrix.ndim)
    )
    
    # Apply the tuple of slices to the matrix
    return matrix[slices]


def np_slice_method4(matrix, axes={}):
    """
    METHOD 4: Using list comprehension (Balanced approach).
    
    Slice a matrix using list comprehension before converting to tuple.
    Balances readability with Pythonic style.
    
    Args:
        matrix (numpy.ndarray): A numpy array of any dimension
        axes (dict, optional): Dictionary of axes to slice
    
    Returns:
        numpy.ndarray: A new sliced numpy array
    
    Example:
        >>> matrix = np.array([[[1, 2, 3], [4, 5, 6]],
        ...                    [[7, 8, 9], [10, 11, 12]]])
        >>> np_slice_method4(matrix, {0: (0, 1), 2: (1, 3)})
        array([[[ 2,  3],
                [ 5,  6]]])
    
    Note:
        - Uses list comprehension for building slices
        - Converts to tuple at the end
        - Balance between Method 1 and Method 2
    """
    
    # Create slices using list comprehension
    # Similar to Method 1 but more Pythonic using comprehension
    # For each dimension i:
    #   - If i in axes: use slice(*axes[i])
    #   - Else: use slice(None)
    slices = [
        slice(*axes[i]) if i in axes else slice(None)
        for i in range(matrix.ndim)
    ]
    
    # Convert list to tuple and apply to matrix
    return matrix[tuple(slices)]


# Example usage and comparison
if __name__ == "__main__":
    # Create test matrix
    matrix = np.array([[[1, 2, 3], [4, 5, 6]],
                       [[7, 8, 9], [10, 11, 12]]])
    
    print("Original matrix shape:", matrix.shape)
    print("Original matrix:\n", matrix)
    
    # Test with axes
    axes = {0: (0, 1), 2: (1, 3)}
    
    print("\n" + "="*50)
    print("Testing all 4 methods with axes:", axes)
    print("="*50)
    
    # All methods should return the same result
    result1 = np_slice(matrix, axes)
    result2 = np_slice_method2(matrix, axes)
    result3 = np_slice_method3(matrix, axes)
    result4 = np_slice_method4(matrix, axes)
    
    print("\nMethod 1 (Loop):\n", result1)
    print("\nMethod 2 (Tuple comprehension):\n", result2)
    print("\nMethod 3 (Using .get()):\n", result3)
    print("\nMethod 4 (List comprehension):\n", result4)
    
    # Verify all methods produce same result
    print("\nAll methods produce same result:", 
          np.array_equal(result1, result2) and 
          np.array_equal(result2, result3) and 
          np.array_equal(result3, result4))
    
    # Test with step value
    print("\n" + "="*50)
    print("Testing with step: axes = {0: (0, 2, 1)}")
    print("="*50)
    axes_with_step = {0: (0, 2, 1)}
    result = np_slice(matrix, axes_with_step)
    print("\nResult:\n", result)
