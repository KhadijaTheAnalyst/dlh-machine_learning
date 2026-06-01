#!/usr/bin/env python3
"""
Module that computes the derivative of a polynomial represented
as a list of coefficients.
"""


def poly_derivative(poly):
    """
    Returns the derivative of a polynomial.

    Args:
        poly (list): coefficients where index = power of x

    Returns:
        list: derivative coefficients, or [0] if derivative is zero,
        or None if invalid input
    """

    if not isinstance(poly, list) or len(poly) == 0:
        return None

    d_poly = [i * poly[i] for i in range(1, len(poly))]

    return d_poly if any(d_poly) else [0]
