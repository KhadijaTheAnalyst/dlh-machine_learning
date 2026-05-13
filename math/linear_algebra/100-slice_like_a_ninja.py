#!/usr/bin/env python3
"""This module to define dynamic method for slicing a matrix with given axes"""

def np_slice(matrix, axes={}):
    """Build slice list, update it, convert to tuple."""
    slices = [slice(None)] * matrix.ndim
    for axis, (start, stop) in axes.items():
        slices[axis] = slice(start, stop)
    return matrix[tuple(slices)]
