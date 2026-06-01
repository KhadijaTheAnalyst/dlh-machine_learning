#!/usr/bin/env python3
"""Integrate a polynomial represented as a list of coefficients."""


def poly_integral(poly, C=0):
    """Compute the integral of a polynomial.

    The polynomial is given as a list where the value at index i is the
    coefficient of x**i. Returns a new list of coefficients for the
    integral, with the integration constant C placed at index 0.

    Args:
        poly (list): coefficients of the polynomial.
        C (int): the integration constant.

    Returns:
        list: coefficients of the integral, or None if inputs are invalid.
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if not all(isinstance(coef, (int, float)) for coef in poly):
        return None
    if not isinstance(C, (int, float)):
        return None

    integral = [C]
    for i in range(len(poly)):
        coef = poly[i] / (i + 1)
        if coef == int(coef):
            coef = int(coef)
        integral.append(coef)

    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    return integral
