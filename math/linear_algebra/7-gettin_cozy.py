#!/usr/bin/env python3
"""
This module provides 2D matrix concatenation functionality
for linear algebra operations.

The module includes:
- cat_matrices2D: Concatenates two 2D matrices along a
specified axis

All functions assume matrices are rectangular
(all rows have the same number of columns).

Author: KMustafa
Date: May 2026
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenate two 2D matrices along a specific axis.

    Joins two 2D matrices either vertically (by rows)
    or horizontally (by columns)
    depending on the axis parameter. Returns a new matrix
    without modifying the
    original matrices.

    Args:
        mat1 (list of lists): First 2D matrix containing
        ints/floats
                             Shape: (rows, columns)
        mat2 (list of lists): Second 2D matrix containing
        ints/floats
                             Shape: (rows, columns)
        axis (int, optional): Direction of concatenation.
        Defaults to 0.
                             - axis=0: Concatenate vertically
                             (stack rows)
                               Requirement: Both matrices must
                               have same number of columns
                             - axis=1: Concatenate horizontally
                             (stack columns)
                               Requirement: Both matrices must have
                               same number of rows

    Returns:
        list of lists: A new concatenated 2D matrix
        if shapes match.
                      Returns None if matrices cannot
                      be concatenated (shape mismatch).

    Raises:
        None (returns None if shapes don't match for the given axis)

    Example:
        >>> mat1 = [[1, 2], [3, 4]]
        >>> mat2 = [[7, 8], [9, 10]]

        >>> # Concatenate vertically (axis=0)
        >>> cat_matrices2D(mat1, mat2, axis=0)
        [[1, 2], [3, 4], [7, 8], [9, 10]]

        >>> # Concatenate horizontally (axis=1)
        >>> cat_matrices2D(mat1, mat2, axis=1)
        [[1, 2, 7, 8], [3, 4, 9, 10]]

        >>> # Shape mismatch example
        >>> mat3 = [[1, 2, 3], [4, 5, 6]]
        >>> cat_matrices2D(mat1, mat3, axis=0)
        None

    Note:
        - Both matrices must be non-empty
        - For axis=0: Both matrices must have the same number of columns
        - For axis=1: Both matrices must have the same number of rows
        - Returns a new matrix (does not modify original matrices)
        - axis=0 is the default parameter
    """

    # ===== AXIS = 0: CONCATENATE VERTICALLY (STACK ROWS) =====
    if axis == 0:
        """
        When axis=0, we stack mat2 BELOW mat1 (vertically).

        Visual example:
        mat1 = [[1, 2],        mat2 = [[7, 8],
                [3, 4]]               [9, 10]]

        Result = [[1, 2],      ← from mat1
                  [3, 4],      ← from mat1
                  [7, 8],      ← from mat2 (added below)
                  [9, 10]]     ← from mat2

        Requirement: Both matrices must have the SAME NUMBER OF COLUMNS
        """

        # Check if the number of columns is the same
        # len(mat1[0]) = number of columns in mat1 (length of first row)
        # len(mat2[0]) = number of columns in mat2 (length of first row)
        if len(mat1[0]) != len(mat2[0]):
            # Columns don't match, cannot concatenate
            return None

        # For axis=0, we can simply use Python's list concatenation
        # This adds all rows from mat2 to the end of mat1
        # mat1 + mat2 combines the two lists of lists
        return mat1 + mat2

    # ===== AXIS = 1: CONCATENATE HORIZONTALLY (STACK COLUMNS) =====
    elif axis == 1:
        """
        When axis=1, we place mat2 NEXT TO mat1 (horizontally).

        Visual example:
        mat1 = [[1, 2],        mat2 = [[7, 8],
                [3, 4]]               [9, 10]]

        Result = [[1, 2, 7, 8],     ← row 0: mat1[0] + mat2[0]
                  [3, 4, 9, 10]]    ← row 1: mat1[1] + mat2[1]

        Requirement: Both matrices must have the SAME NUMBER OF ROWS
        """

        # Check if the number of rows is the same
        # len(mat1) = number of rows in mat1
        # len(mat2) = number of rows in mat2
        if len(mat1) != len(mat2):
            # Rows don't match, cannot concatenate
            return None

        # Create an empty list to store the result matrix
        # This will contain all the concatenated rows
        new_matrix = []

        # Loop through each ROW
        # i = row index (0, 1, 2, ...)
        for i in range(len(mat1)):
            # Get row i from mat1 and row i from mat2
            # Concatenate them using the + operator
            # mat1[i] = first row (e.g., [1, 2])
            # mat2[i] = second row (e.g., [7, 8])
            # mat1[i] + mat2[i] = concatenated row (e.g., [1, 2, 7, 8])
            concatenated_row = mat1[i] + mat2[i]

            # Add the concatenated row to the new matrix
            new_matrix.append(concatenated_row)

        # Return the complete matrix with all concatenated rows
        return new_matrix

    # If axis is neither 0 nor 1, return None (invalid axis)
    return None
