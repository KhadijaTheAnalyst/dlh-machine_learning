#!/usr/bin/env python3
"""
This module provides matrix multiplication functionality
for linear algebra operations.

The module includes:
- mat_mul: Performs matrix multiplication on two 2D matrices

All functions assume matrices are rectangular
(all rows have the same number of columns).

Author: KMustafa
Date: May 2026
"""


def mat_mul(mat1, mat2):
    """
    Perform matrix multiplication on two 2D matrices.

    Multiplies two 2D matrices using the standard matrix
    multiplication algorithm.
    Each element in the result is calculated by taking
    the dot product of a row
    from mat1 and a column from mat2.

    Args:
        mat1 (list of lists): First 2D matrix containing ints/floats
                             Shape: (rows1, cols1)
        mat2 (list of lists): Second 2D matrix containing ints/floats
                             Shape: (rows2, cols2)

    Returns:
        list of lists: A new 2D matrix (result of multiplication)
        if multiplication
                      is possible. Returns None if matrices
                      cannot be multiplied.
                      Result shape: (rows1, cols2)

    Raises:
        None (returns None if matrices cannot be multiplied)

    Multiplication Requirements:
        - Number of COLUMNS in mat1 must equal number of
        ROWS in mat2
        - cols1 == rows2 (mathematical requirement for
        matrix multiplication)

    How It Works:
        Result[i][j] = (Row i of mat1) · (Column j of mat2)

        The dot product is calculated as:
        Row [a, b, c] · Column [x, y, z] = (a*x) + (b*y) + (c*z)

    Example:
        >>> mat1 = [[1, 2],
        ...         [3, 4],
        ...         [5, 6]]
        >>> mat2 = [[1, 2, 3, 4],
        ...         [5, 6, 7, 8]]

        >>> mat_mul(mat1, mat2)
        [[11, 14, 17, 20], [23, 30, 37, 44], [35, 46, 57, 68]]

        >>> # Cannot multiply - columns of mat1 (2) != rows of mat2 (3)
        >>> mat3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> mat_mul(mat1, mat3)
        None

    Note:
        - Creates a new matrix (does not modify original matrices)
        - Result shape: (number of rows from mat1)
        ×
        (number of columns from mat2)
        - Matrix multiplication is NOT commutative:
        mat_mul(A, B) ≠ mat_mul(B, A)
    """

    # ===== SHAPE CHECKING =====
    # For matrix multiplication to work: cols1 must equal rows1
    # len(mat1[0]) = number of columns in mat1 (length of first row)
    # len(mat2) = number of rows in mat2 (length of the matrix)

    if len(mat1[0]) != len(mat2):
        # Cannot multiply - shapes are incompatible
        return None

    # ===== CREATE RESULT MATRIX =====
    # Result shape: (rows of mat1) × (columns of mat2)
    # len(mat1) = number of rows in mat1
    # len(mat2[0]) = number of columns in mat2 (length of first row)
    new_matrix = []

    # ===== FIRST LOOP: For each ROW in mat1 =====
    # i = row index in mat1 (0, 1, 2, ...)
    # We will create one row in the result for each row in mat1
    for i in range(len(mat1)):

        # Create an empty list to store the result for this row
        # This will contain one element for each column in mat2
        new_row = []

        # ===== SECOND LOOP: For each COLUMN in mat2 =====
        # j = column index in mat2 (0, 1, 2, ...)
        # We will create one element in new_row for each column in mat2
        for j in range(len(mat2[0])):

            # Initialize sum to 0
            # This will store the dot product (sum of products)
            sum_product = 0

            # ===== THIRD LOOP: Calculate dot product =====
            # k = position in the row and column
            # Multiply corresponding elements from row i and column j
            # Then add them all together
            for k in range(len(mat1[i])):

                # mat1[i][k] = element k in row i of mat1
                # mat2[k][j] = element in row k, column j of mat2
                # (This is the element in column j of mat2)

                # Example:
                # Row [1, 2] · Column [5, 6]
                # k=0: mat1[i][0] * mat2[0][j] = 1 * 5 = 5
                # k=1: mat1[i][1] * mat2[1][j] = 2 * 6 = 12
                # sum_product = 5 + 12 = 17

                sum_product += mat1[i][k] * mat2[k][j]

            # After calculating the dot product for column j,
            # append it to the new_row
            new_row.append(sum_product)

        # After processing all columns (j loop done),
        # append the completed row to the result matrix
        new_matrix.append(new_row)

    # After processing all rows (i loop done),
    # return the complete result matrix
    return new_matrix
