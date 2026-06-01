#!/usr/bin/env python3
"""
Module for computing the sum of squares of the first n natural numbers.
"""


def summation_i_squared(n):
    """
    Compute the sum of squares from 1 to n.

    The function returns:
        1^2 + 2^2 + 3^2 + ... + n^2

    Uses the mathematical formula:
        n(n + 1)(2n + 1) / 6

    Args:
        n (int): The upper limit of the summation (must be a positive integer)

    Returns:
        int: Sum of squares from 1 to n
        None: If n is not a valid positive integer
    """
    if not isinstance(n, int) or n <= 0:
        return None

    return (n * (n + 1) * (2 * n + 1)) // 6
