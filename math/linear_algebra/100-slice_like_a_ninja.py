#!/usr/bin/env python3
"""This module to define dynamic method for slicing a matrix with given axes"""

def np_slice(matrix, axes={}):
    """Build slice list, update it, convert to tuple."""
    slices = [slice(None)] * matrix.ndim
    for axis, slice_tuple in axes.items():
        slices[axis] = slice(*slice_tuple)  # ✅ Handles 2 or 3 values!
    return matrix[tuple(slices)]
