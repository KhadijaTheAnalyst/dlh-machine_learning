#!/usr/bin/env python3
"""Calculates the likelihood of obtaining data given various
hypothetical probabilities."""
import numpy as np
import math


def likelihood(x, n, P):
    """
    Calculates the likelihood of obtaining this data given
    various hypothetical probabilities of developing severe
    side effects.

    x: number of patients that develop severe side effects
    n: total number of patients observed
    P: 1D numpy.ndarray containing the various hypothetical
       probabilities of developing severe side effects

    Returns: 1D numpy.ndarray containing the likelihood of
             obtaining the data, x and n, for each
             probability in P
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")

    # binomial coefficient: n! / (x! * (n-x)!)
    fact_n = math.factorial(n)
    fact_x = math.factorial(x)
    fact_nx = math.factorial(n - x)
    binom_coeff = fact_n / (fact_x * fact_nx)

    likelihoods = binom_coeff * (P ** x) * ((1 - P) ** (n - x))
    return likelihoods
