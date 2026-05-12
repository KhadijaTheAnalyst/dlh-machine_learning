#!/usr/bin/env python3
"""
This module provides array addition functionality.

The module includes:
- add_arrays: Adds two arrays element-wise

Author: KMustafa
Date: May 2026
"""


def add_arrays(arr1, arr2):
    """
    Add two arrays element-wise.

    Takes two arrays and returns a new array where each
    element is the sum
    of the corresponding elements from arr1 and arr2.

    Args:
        arr1 (list): First array of ints/floats
        arr2 (list): Second array of ints/floats

    Returns:
        list: A new list with element-wise sums, or None if shapes don't match

    Raises:
        None (returns None if arrays have different lengths)

    Example:
        >>> add_arrays([1, 2, 3, 4], [5, 6, 7, 8])
        [6, 8, 10, 12]

        >>> add_arrays([1, 2, 3], [4, 5])
        None

    Note:
        - Both arrays must have the same length
        - Returns a new list (does not modify original arrays)
    """

    # Check if arrays have the same shape (length)
    if len(arr1) != len(arr2):
        return None

    # METHOD 1: Using zip() - RECOMMENDED (Cleaner & Pythonic)
    # =========================================================
    # zip(arr1, arr2)  # Pairs them: (1,5), (2,6), (3,7), (4,8)
    result = []
    for a, b in zip(arr1, arr2):
        result.append(a + b)
    return result

    # METHOD 2: Using index - ALTERNATIVE (More Traditional)
    # ======================================================
    # Uncomment below to see the index-based approach
    # new_list = []
    # for i in range(len(arr1)):
    #     new_list.append(arr1[i] + arr2[i])
    # return new_list
