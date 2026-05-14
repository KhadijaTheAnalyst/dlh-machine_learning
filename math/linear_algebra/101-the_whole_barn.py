#!/usr/bin/env python3
"""Module fot adding two matrices using recursion"""


def add_matrices(mat1, mat2):
    """THIS FUNCTION ADD TWO MATRICES OF SAME SHAPE"""

    if len(mat1) != len(mat2):
        return None

    result = []

    for i in range(len(mat1)):
        if isinstance(mat1[i], list):
            add_it = add_matrices(mat1[i], mat2[i])
            if add_it is None:
                return None
            result.append(add_it)
        else:
            result.append(mat1[i] + mat2[i])
    return result
