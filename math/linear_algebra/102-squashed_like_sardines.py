#!/usr/bin/env python3
"""This module contains the recursive function to concatenate nD matrices """

def cat_any_axis_recursive(mat1, mat2, axis=0):
    """Function to concatenate matrices """
    if axis == 0:
        return list(mat1) + list(mat2)

    result = []
    for i in range(len(mat1)):
        concatenated = cat_any_axis_recursive(mat1[i], mat2[i], axis - 1)
        result.append(concatenated)

    return result
