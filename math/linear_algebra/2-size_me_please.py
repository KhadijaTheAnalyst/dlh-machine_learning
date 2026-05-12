#!/usr/bin/env python3
"""
This program defines a function matrix_shape that takes a
matrix as input and returns a tuple containing the number of
rows and columns in the matrix.
The function should work for matrices of any size, including
empty matrices and matrices with only one row or one column.
"""


def matrix_shape(matrix):
    """
    Returns the shape of a matrix as a list of integers.
    The shape of a matrix is the number of rows and columns
    in the matrix.
    args:
        matrix: A list of lists representing a matrix.
        returns: A list of integers representing the shape
        of the matrix.
        """

    shape = [len(matrix)]
    if isinstance(matrix[0], list):
        shape += matrix_shape(matrix[0])
    return shape
