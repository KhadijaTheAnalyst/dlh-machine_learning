#!/usr/bin/env python3
"""
Module that contains a function for adding two 2D matrices.

The function adds matrices element-by-element and returns
a new matrix containing the results.
"""


def add_matrices2D(mat1, mat2):
    """
    Add two 2D matrices element-wise.

    Args:
        mat1 (list of lists): First 2D matrix containing integers/floats.
        mat2 (list of lists): Second 2D matrix containing integers/floats.

    Returns:
        list of lists:
            A new matrix containing the sum of corresponding elements.
        None:
            If the matrices do not have the same shape.

    Example:
        >>> mat1 = [[1, 2], [3, 4]]
        >>> mat2 = [[5, 6], [7, 8]]
        >>> add_matrices2D(mat1, mat2)
        [[6, 8], [10, 12]]
    """

    # Check if both matrices have the same number of rows
    if len(mat1) != len(mat2) and len(mat[0]) != len(mat[0]):
        return None

    # Check if each corresponding row has the same length
    for i in range(len(mat1)):
        if len(mat1[i]) != len(mat2[i]):
            return None

    # Create a new matrix to store the result
    result = []

    # Loop through rows
    for i in range(len(mat1)):
        row = []

        # Loop through columns
        for j in range(len(mat1[i])):
            # Add corresponding elements
            row.append(mat1[i][j] + mat2[i][j])

        # Add completed row to result matrix
        result.append(row)

    return result

# Can add two matrices using zip as well.
# result = []
# for row1, row2 in zip(mat1, mat2):
# new_row = []
# for val1, val2 in zip(row1, row2):
# new_row.append(val1 + val2)
# result.append(new_row)

# Can add two matrices using enumerate as well.
# for i, row in enumerate(mat1):
# new_row = []
# for j, value in enumerate(row):
# new_row.append(value + mat2[i][j])
# result.append(new_row)
