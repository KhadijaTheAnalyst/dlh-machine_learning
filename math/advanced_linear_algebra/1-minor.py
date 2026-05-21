#!/usr/bin/env python3
"""
Advanced Linear Algebra Module

This module provides functions for working with square matrices,
including computation of determinants and minor matrices.

Functions:
    - determinant(matrix): Computes the determinant of a square matrix
    - minor(matrix): Computes the minor matrix of a square matrix

Both functions assume the input is a valid square matrix represented
as a list of lists.

Validation rules:
    - Input must be a list of lists
    - Matrix must be non-empty
    - Matrix must be square (same number of rows and columns)

Note:
    The determinant function uses recursive cofactor expansion for
    matrices larger than 2x2.
"""


def determinant(matrix):
    """
    Calculate the determinant of a square matrix.

    Uses direct calculation for small matrices (1×1, 2×2) and recursive
    cofactor expansion for larger matrices (3×3+).

    Args:
        matrix (list of lists): A square matrix represented as a list of lists,
                                where each inner list is a row.

    Returns:
        int or float: The determinant of the matrix.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not square (rows ≠ columns).

    Note:
        - The list [[]] represents a 0×0 matrix with determinant = 1
        - Empty list [] raises TypeError
    """

    # ========== VALIDATION SECTION ==========
    # Check if matrix itself is a list
    if isinstance(matrix, list):
        if len(matrix) == 0:
            raise TypeError("matrix must be a list of lists")
    else:
        raise TypeError("matrix must be a list of lists")

    # Check if each element in matrix is a list
    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
            raise TypeError("matrix must be a list of lists")

    # Check if all rows have the same length
    for i in matrix:
        if len(i) != len(matrix[0]):
            raise ValueError("matrix must be a square matrix")

    # ========== SPECIAL CASES SECTION ==========
    # Special case: 0×0 matrix (represented as [[]])
    if len(matrix[0]) == 0:
        return 1

    # Check if matrix is square (rows = columns)
    elif len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a square matrix")

    # ========== BASE CASES SECTION ==========
    # Base case: 1×1 matrix, determinant is the single element
    elif len(matrix[0]) == 1:
        return matrix[0][0]

    # Base case: 2×2 matrix, use direct formula: (a*d) - (b*c)
    elif len(matrix) == 2:
        det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        return det

    # ========== RECURSIVE CASE SECTION ==========
    # Recursive case: n×n matrix (n > 2), use cofactor expansion
    else:
        det = 0

        # Loop through each column in the first row
        for column in range(len(matrix[0])):
            # Create a minor: matrix with row 0 and current column removed
            minor = []
            for i in range(1, len(matrix)):
                new_row = []
                for j in range(len(matrix[i])):
                    if j != column:
                        new_row.append(matrix[i][j])
                minor.append(new_row)

            # Calculate the sign: alternates (+1, -1, +1, -1, ...)
            sign = (-1) ** column

            # Add the cofactor contribution:
            # element * sign * determinant(minor)
            det += matrix[0][column] * sign * determinant(minor)

        return det


def minor(matrix):
    """
    Compute the minor matrix of a square matrix.

    The minor matrix is formed by calculating the determinant of the
    submatrix obtained by removing one row and one column for each
    element in the original matrix.

    Args:
        matrix (list of lists): A square matrix represented as a list of lists.

    Returns:
        list of lists: The minor matrix, where each element (i, j) is the
        determinant of the matrix formed by removing row i and column j
        from the original matrix.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is empty or not a square matrix.

    Special case:
        If the matrix is 1x1, returns [[1]].
    """

    # Special case: 1x1 matrix
    # The minor of a single element is defined as [[1]]
    if len(matrix) == 1:
        return [[1]]

    result = []  # This will store the final minor matrix

    # Loop through each row (i = row index to remove)
    for i in range(len(matrix)):

        row = []  # This will store one row of the result matrix

        # Loop through each column (j = column index to remove)
        for j in range(len(matrix[i])):

            minor = []  # This will store the submatrix for (i, j)

            # Build the submatrix by skipping row i
            for r in range(len(matrix)):

                if r != i:  # skip the row being excluded

                    new_row = []

                    # Build each row of the submatrix by skipping column j
                    for c in range(len(matrix)):

                        if c != j:  # skip the column being excluded
                            new_row.append(matrix[r][c])

                    minor.append(new_row)  # add processed row to submatrix

            # Compute determinant of the submatrix and store it
            row.append(determinant(minor))

        # Add completed row to result matrix
        result.append(row)

    return result
