#!/usr/bin/env python3
"""
This program defines a function matrix_shape that takes a
matrix as input and returns a tuple containing the number of
rows and columns in the matrix.
The function should work for matrices of any size, including
empty matrices and matrices with only one row or one column.
"""


def matrix_shape(matrix):
    """Returns the number of rows and columns of a matrix as a tuple (num_rows, num_cols)"""
    shape = [len(matrix)]
    if isinstance(matrix[0], list):
        shape += matrix_shape(matrix[0])
    return shape
