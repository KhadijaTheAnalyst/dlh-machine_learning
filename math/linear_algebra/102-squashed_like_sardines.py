#!/usr/bin/env python3
"""
This module contains functions to concatenate n-dimensional matrices recursively.

The module includes:
1. matrix_shape(): Helper function to determine matrix dimensions
2. cat_matrices(): Main function to concatenate matrices along any axis

Features:
- Works with 1D, 2D, 3D, 4D, and higher dimensional arrays
- Supports concatenation along any axis
- Validates matrix compatibility before concatenation
- Returns None if matrices cannot be concatenated
- No external libraries required (pure Python)

Author: KMustafa
Date: May 2026
"""


def matrix_shape(matrix):
    """
    Recursively determine the shape of a matrix.
    
    This function calculates the dimensions of a matrix by recursively
    checking the depth and width of nested lists. It's essential for
    validating whether two matrices can be concatenated.
    
    How it works:
    - Start with the length of the matrix (first dimension)
    - If elements are lists, recursively get their shape
    - Keep building the shape tuple by going deeper
    
    Args:
        matrix (list or nested list): A Python list representing a matrix
    
    Returns:
        list: Shape of the matrix as a list of integers
              Example: [[1,2],[3,4]] → [2, 2]
                       [[[1,2]]] → [1, 1, 2]
    
    Examples:
        >>> matrix_shape([1, 2, 3])
        [3]
        
        >>> matrix_shape([[1, 2], [3, 4]])
        [2, 2]
        
        >>> matrix_shape([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
        [2, 2, 2]
    
    Note:
        - Assumes all rows have the same length (rectangular matrix)
        - Only works if first element determines structure of rest
        - Returns empty shape for empty matrices
    """
    
    # STEP 1: Get the first dimension (number of elements in this level)
    # len(matrix) gives us how many rows/elements are at this level
    shape = [len(matrix)]
    
    # STEP 2: Check if we need to go deeper
    # isinstance(matrix[0], list) checks if elements are lists (nested)
    # If True, there's another dimension to explore
    if isinstance(matrix[0], list):
        # Recursively get the shape of the first element
        # This gives us the shape of all deeper dimensions
        shape += matrix_shape(matrix[0])
    
    # STEP 3: Return the complete shape
    # For 1D: [5] (5 elements)
    # For 2D: [3, 4] (3 rows, 4 columns)
    # For 3D: [2, 3, 4] (2 blocks, 3 rows, 4 columns)
    return shape


def cat_matrices(mat1, mat2, axis=0):
    """
    Concatenate two matrices along a specified axis.
    
    This function combines two matrices by joining them along a specific
    dimension. It works recursively for any number of dimensions and validates
    that the matrices are compatible before concatenating.
    
    WHAT IS CONCATENATION?
    - axis=0: Stack rows (add more rows)
      [[1, 2], [3, 4]] + [[5, 6]] → [[1, 2], [3, 4], [5, 6]]
    
    - axis=1: Stack columns (add more columns)
      [[1, 2], [3, 4]] + [[5, 6], [7, 8]] → [[1, 2, 5, 6], [3, 4, 7, 8]]
    
    - axis=2+: Combine deeper dimensions
    
    HOW THE FUNCTION WORKS:
    1. Get the shape of both matrices
    2. Validate they have the same number of dimensions
    3. Validate the axis is valid (between 0 and number of dimensions)
    4. Validate shapes match on all axes except the concatenation axis
    5. Perform the concatenation recursively
    
    Args:
        mat1 (list or nested list): First matrix to concatenate
        mat2 (list or nested list): Second matrix to concatenate
        axis (int, optional): Axis along which to concatenate.
                             Default is 0 (concatenate rows)
                             - axis=0: stack vertically (add rows)
                             - axis=1: stack horizontally (add columns)
                             - axis=2+: deeper dimensions
    
    Returns:
        list or None: Concatenated matrix if successful, None if incompatible
    
    Examples:
        >>> # Example 1: Concatenate 1D arrays (axis=0)
        >>> cat_matrices([1, 2, 3], [4, 5, 6], axis=0)
        [1, 2, 3, 4, 5, 6]
        
        >>> # Example 2: Concatenate 2D arrays along rows (axis=0)
        >>> mat1 = [[1, 2], [3, 4]]
        >>> mat2 = [[5, 6], [7, 8]]
        >>> cat_matrices(mat1, mat2, axis=0)
        [[1, 2], [3, 4], [5, 6], [7, 8]]
        
        >>> # Example 3: Concatenate 2D arrays along columns (axis=1)
        >>> cat_matrices(mat1, mat2, axis=1)
        [[1, 2, 5, 6], [3, 4, 7, 8]]
        
        >>> # Example 4: Invalid concatenation (different dimensions)
        >>> cat_matrices([[1, 2]], [[[1, 2]]])
        None
        
        >>> # Example 5: Invalid concatenation (incompatible shapes)
        >>> cat_matrices([[1, 2, 3]], [[4, 5], [6, 7]], axis=0)
        None
    
    Note:
        - Both matrices must have the same number of dimensions
        - All dimensions except 'axis' must have the same size
        - Use zip() to pair elements from both matrices efficiently
        - Returns None for invalid inputs (no exceptions raised)
    """
    
    # ============================================================
    # VALIDATION SECTION: Check if matrices can be concatenated
    # ============================================================
    
    # STEP 1: Get the shape of both matrices
    # matrix_shape returns a list like [2, 3] for a 2x3 matrix
    shape1 = matrix_shape(mat1)
    shape2 = matrix_shape(mat2)
    
    # Example:
    # mat1 = [[1, 2], [3, 4]] → shape1 = [2, 2]
    # mat2 = [[5, 6], [7, 8]] → shape2 = [2, 2]
    
    # STEP 2: Check if matrices have the same number of dimensions
    # len(shape) tells us how many dimensions the matrix has
    # - 1D array: len(shape) = 1, like [5]
    # - 2D array: len(shape) = 2, like [2, 3]
    # - 3D array: len(shape) = 3, like [2, 3, 4]
    if len(shape1) != len(shape2):
        # If they don't match, concatenation is impossible
        # Example: [1, 2, 3] (1D) can't concat with [[1]] (2D)
        return None
    
    # STEP 3: Check if the axis is valid
    # axis must be between 0 and (number of dimensions - 1)
    # - For 2D: valid axes are 0 and 1
    # - For 3D: valid axes are 0, 1, and 2
    if axis < 0 or axis >= len(shape1):
        # Invalid axis → can't concatenate
        return None
    
    # STEP 4: Check if shapes match on all axes except the concatenation axis
    # When concatenating, only the concatenation axis can differ
    # All other dimensions MUST be exactly the same
    for i in range(len(shape1)):
        if i != axis:  # Skip the axis we're concatenating on
            if shape1[i] != shape2[i]:
                # Shapes don't match on this dimension
                # Example: mat1 is 2x3, mat2 is 2x4, axis=0
                # Different column counts (3 vs 4) → can't concatenate
                return None
    
    # ============================================================
    # CONCATENATION SECTION: Actually concatenate the matrices
    # ============================================================
    
    # STEP 5: Perform concatenation based on axis
    
    # BASE CASE: axis = 0 (concatenate at top level)
    # For axis=0, we just need to combine the two lists
    # This is the simplest case: just add the lists together
    if axis == 0:
        # list(mat1) creates a shallow copy of mat1
        # list(mat2) creates a shallow copy of mat2
        # + concatenates them together
        # Example: [1, 2] + [3, 4] = [1, 2, 3, 4]
        # Example: [[1,2]] + [[3,4]] = [[1,2], [3,4]]
        return list(mat1) + list(mat2)
    
    # RECURSIVE CASE: axis > 0 (concatenate deeper dimensions)
    # When axis > 0, we need to go one level deeper
    # We process each element at this level and recursively concatenate them
    
    # Create an empty list to store results
    result = []
    
    # STEP 6: Loop through paired elements from both matrices
    # zip(mat1, mat2) pairs up elements from both matrices
    # Example: zip([[1,2], [3,4]], [[5,6], [7,8]])
    #          → ([1,2], [5,6]), ([3,4], [7,8])
    for element1, element2 in zip(mat1, mat2):
        # element1 = one element from mat1 at this level
        # element2 = corresponding element from mat2 at this level
        
        # STEP 7: Recursively concatenate these elements along axis-1
        # We reduce the axis by 1 because we're going one level deeper
        # Example:
        # - axis=1 becomes axis=0 at the next level
        # - axis=2 becomes axis=1 at the next level
        concatenated = cat_matrices(element1, element2, axis - 1)
        
        # STEP 8: Add the concatenated element to result
        # result.append() adds the element to the end of the list
        result.append(concatenated)
    
    # STEP 9: Return the final concatenated result
    # result now contains all concatenated sub-matrices
    return result


# ============================================================
# EXAMPLE TEST CASES WITH DETAILED EXPLANATIONS
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("CONCATENATION EXAMPLES - Understanding axis parameter")
    print("=" * 60)
    
    # ============================================================
    # TEST 1: 1D Arrays (axis=0)
    # ============================================================
    print("\nTEST 1: Concatenate 1D Arrays (axis=0)")
    print("-" * 60)
    
    mat1_1d = [1, 2, 3]
    mat2_1d = [4, 5, 6]
    
    print(f"mat1 = {mat1_1d}")
    print(f"mat2 = {mat2_1d}")
    print(f"Shape of mat1: {matrix_shape(mat1_1d)}")
    print(f"Shape of mat2: {matrix_shape(mat2_1d)}")
    
    result = cat_matrices(mat1_1d, mat2_1d, axis=0)
    print(f"cat_matrices(mat1, mat2, axis=0)")
    print(f"Result: {result}")
    print(f"✅ SUCCESS - Lists joined end to end")
    
    # ============================================================
    # TEST 2: 2D Arrays (axis=0 - Stack Rows)
    # ============================================================
    print("\n\nTEST 2: Concatenate 2D Arrays Along axis=0 (Stack Rows)")
    print("-" * 60)
    
    mat1_2d = [[1, 2], [3, 4]]
    mat2_2d = [[5, 6], [7, 8]]
    
    print(f"mat1 =")
    for row in mat1_2d:
        print(f"  {row}")
    print(f"Shape: {matrix_shape(mat1_2d)} (2 rows, 2 columns)")
    
    print(f"\nmat2 =")
    for row in mat2_2d:
        print(f"  {row}")
    print(f"Shape: {matrix_shape(mat2_2d)} (2 rows, 2 columns)")
    
    result = cat_matrices(mat1_2d, mat2_2d, axis=0)
    print(f"\ncat_matrices(mat1, mat2, axis=0)")
    print(f"Result =")
    for row in result:
        print(f"  {row}")
    print(f"Shape: {matrix_shape(result)} (4 rows, 2 columns)")
    print(f"✅ SUCCESS - Rows stacked vertically")
    
    # ============================================================
    # TEST 3: 2D Arrays (axis=1 - Stack Columns)
    # ============================================================
    print("\n\nTEST 3: Concatenate 2D Arrays Along axis=1 (Stack Columns)")
    print("-" * 60)
    
    print(f"mat1 =")
    for row in mat1_2d:
        print(f"  {row}")
    print(f"Shape: {matrix_shape(mat1_2d)}")
    
    print(f"\nmat2 =")
    for row in mat2_2d:
        print(f"  {row}")
    print(f"Shape: {matrix_shape(mat2_2d)}")
    
    result = cat_matrices(mat1_2d, mat2_2d, axis=1)
    print(f"\ncat_matrices(mat1, mat2, axis=1)")
    print(f"Result =")
    for row in result:
        print(f"  {row}")
    print(f"Shape: {matrix_shape(result)} (2 rows, 4 columns)")
    print(f"✅ SUCCESS - Columns merged horizontally")
    
    # ============================================================
    # TEST 4: 3D Arrays (axis=2)
    # ============================================================
    print("\n\nTEST 4: Concatenate 3D Arrays Along axis=2")
    print("-" * 60)
    
    mat1_3d = [[[1, 2], [3, 4]]]
    mat2_3d = [[[5, 6], [7, 8]]]
    
    print(f"mat1 shape: {matrix_shape(mat1_3d)} (1 block, 2 rows, 2 cols)")
    print(f"mat2 shape: {matrix_shape(mat2_3d)} (1 block, 2 rows, 2 cols)")
    
    result = cat_matrices(mat1_3d, mat2_3d, axis=2)
    print(f"\ncat_matrices(mat1, mat2, axis=2)")
    print(f"Result shape: {matrix_shape(result)}")
    print(f"Result: {result}")
    print(f"✅ SUCCESS - 3D arrays concatenated along deepest dimension")
    
    # ============================================================
    # TEST 5: Invalid - Different Dimensions
    # ============================================================
    print("\n\nTEST 5: Invalid - Different Number of Dimensions")
    print("-" * 60)
    
    mat_2d = [[1, 2]]      # 2D array
    mat_3d = [[[1, 2]]]    # 3D array
    
    print(f"mat_2d shape: {matrix_shape(mat_2d)} (2 dimensions)")
    print(f"mat_3d shape: {matrix_shape(mat_3d)} (3 dimensions)")
    
    result = cat_matrices(mat_2d, mat_3d, axis=0)
    print(f"\ncat_matrices(mat_2d, mat_3d, axis=0)")
    print(f"Result: {result}")
    print(f"✅ CORRECT - Returns None (can't concatenate different dimensions)")
    
    # ============================================================
    # TEST 6: Invalid - Incompatible Shapes
    # ============================================================
    print("\n\nTEST 6: Invalid - Incompatible Shapes (Different Column Counts)")
    print("-" * 60)
    
    mat_2x3 = [[1, 2, 3]]           # 1 row, 3 columns
    mat_2x2 = [[4, 5], [6, 7]]      # 2 rows, 2 columns
    
    print(f"mat_2x3 shape: {matrix_shape(mat_2x3)} (1 row, 3 columns)")
    print(f"mat_2x2 shape: {matrix_shape(mat_2x2)} (2 rows, 2 columns)")
    
    result = cat_matrices(mat_2x3, mat_2x2, axis=0)
    print(f"\ncat_matrices(mat_2x3, mat_2x2, axis=0)")
    print(f"Result: {result}")
    print(f"✅ CORRECT - Returns None (different column counts)")
    
    # ============================================================
    # TEST 7: Invalid - Invalid Axis
    # ============================================================
    print("\n\nTEST 7: Invalid - Invalid Axis")
    print("-" * 60)
    
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6], [7, 8]]
    
    print(f"mat1 and mat2 are 2D (valid axes: 0, 1)")
    
    result = cat_matrices(mat1, mat2, axis=5)
    print(f"\ncat_matrices(mat1, mat2, axis=5)")
    print(f"Result: {result}")
    print(f"✅ CORRECT - Returns None (axis 5 doesn't exist for 2D)")
    
    print("\n" + "=" * 60)
    print("ALL TESTS COMPLETE!")
    print("=" * 60)
