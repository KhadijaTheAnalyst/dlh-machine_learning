#!/usr/bin/env python3

def add_matrices(mat1, mat2):
    """
    Recursively adds two matrices of any dimension.

    A matrix can be:
    - 1D: [1, 2, 3]
    - 2D: [[1, 2], [3, 4]]
    - 3D, 4D, etc.

    The function works by:
    1. Checking if both matrices have the same shape
    2. Going deeper into nested lists using recursion
    3. Adding numbers when the deepest level is reached

    Args:
        mat1: First matrix (list)
        mat2: Second matrix (list)

    Returns:
        A new matrix containing the sums
        OR
        None if matrices do not have the same shape
    """

    # Check if current level has same length
    # Example:
    # [1, 2, 3] and [4, 5]
    # Different sizes -> return None
    if len(mat1) != len(mat2):
        return None

    # Create empty list to store final result
    result = []

    # Loop through every element in matrix
    for i in range(len(mat1)):

        # Check if current element is another list
        # This means matrix still has deeper dimensions
        #
        # Example:
        # mat1[i] = [1, 2]
        #
        # Since it is a list, we must go deeper
        # into the matrix using recursion
        if type(mat1[i]) == list:

            # Recursive call
            #
            # Function calls itself on smaller sub-matrices
            #
            # Example:
            # [[1,2],[3,4]]
            #
            # first recursive call becomes:
            # [1,2]
            #
            # then eventually reaches numbers
            added = add_matrices(mat1[i], mat2[i])

            # If deeper matrices do not match shape
            # stop everything and return None
            if added is None:
                return None

            # Store returned sub-matrix into result
            #
            # Example:
            # result.append([6,8])
            result.append(added)

        # If element is NOT a list,
        # then we reached actual numbers
        #
        # Example:
        # 1 + 5
        else:

            # Add numbers and store result
            result.append(mat1[i] + mat2[i])

    # Return fully completed matrix
    return result
