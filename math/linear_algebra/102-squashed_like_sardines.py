#!/usr/bin/env python3
"""Concatenate matrices without NumPy"""


def matrix_shape(matrix):
    """Get the shape of a matrix recursively."""
    shape = [len(matrix)]
    if isinstance(matrix[0], list):
        shape += matrix_shape(matrix[0])
    return shape


def cat_matrices(mat1, mat2, axis=0):
    """Concatenate two matrices along a specified axis."""

    # Get shapes
    shape1 = matrix_shape(mat1)
    shape2 = matrix_shape(mat2)

    # Check 1: Same number of dimensions?
    if len(shape1) != len(shape2):
        return None

    # Check 2: Valid axis?
    if axis < 0 or axis >= len(shape1):
        return None

    # Check 3: Compatible shapes?
    for i in range(len(shape1)):
        if i != axis:
            if shape1[i] != shape2[i]:
                return None

    # Concatenate
    if axis == 0:
        return list(mat1) + list(mat2)

    result = []
    for element1, element2 in zip(mat1, mat2):
        concatenated = cat_matrices(element1, element2, axis - 1)
        result.append(concatenated)

    return result

# # Test cases
# print("Test 1 (2D, axis=0):")
# m1 = [[1, 2], [3, 4]]
# m2 = [[5, 6], [7, 8]]
# print(cat_matrices(m1, m2, axis=0))
# # [[1, 2], [3, 4], [5, 6], [7, 8]] ✅

# print("\nTest 2 (2D, axis=1):")
# print(cat_matrices(m1, m2, axis=1))
# # [[1, 2, 5, 6], [3, 4, 7, 8]] ✅

# print("\nTest 3 (Different dimensions):")
# m3 = [[1, 2]]  # 2D
# m4 = [[[1, 2]]]  # 3D
# print(cat_matrices(m3, m4))
# # None ✅

# print("\nTest 4 (Incompatible shapes):")
# m5 = [[1, 2, 3]]  # Shape: (1, 3)
# m6 = [[4, 5], [6, 7]]  # Shape: (2, 2)
# print(cat_matrices(m5, m6, axis=0))
# # None ✅
