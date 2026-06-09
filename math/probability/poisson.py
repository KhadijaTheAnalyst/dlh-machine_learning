#!/usr/bin/env python3
"""Module for the Poisson distribution class."""


class Poisson:
    """Represents a Poisson distribution.

    The Poisson distribution models the probability of a given number
    of events occurring in a fixed interval of time or space, given a
    known average rate of occurrence (lambda).

    Attributes:
        lambtha (float): The expected number of occurrences in a given
            time frame (rate parameter).
    """

    def __init__(self, data=None, lambtha=1.):
        """Initializes a Poisson distribution.

        Args:
            data (list, optional): A list of data points used to estimate
                the distribution's lambda. Defaults to None.
            lambtha (float, optional): The expected number of occurrences.
                Used only if data is None. Defaults to 1.0.

        Raises:
            ValueError: If lambtha is not a positive value.
            TypeError: If data is not a list.
            ValueError: If data does not contain multiple values.
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """Calculates the value of the PMF for a given number of successes.

        The Poisson PMF is defined as:
            P(X = k) = (e^(-lambda) * lambda^k) / k!

        Args:
            k (int): The number of successes. Non-integers are converted
                to integers. Negative values return 0.

        Returns:
            float: The PMF value for k, or 0 if k is out of range.
        """
        if not isinstance(k, int):
            k = int(k)

        if k < 0:
            return 0

        e = 2.7182818285

        e_neg_lambda = e ** (-self.lambtha)
        lambda_k = self.lambtha ** k

        k_factorial = 1
        for i in range(1, k + 1):
            k_factorial *= i

        return (e_neg_lambda * lambda_k) / k_factorial

    def cdf(self, k):
         """Calculates the value of the CDF for a given number of successes.

        The Poisson CDF is the cumulative sum of the PMF from 0 through k:
            P(X <= k) = sum_{i=0}^{k} (e^(-lambda) * lambda^i) / i!

        Args:
            k (int): The number of successes. Non-integers are converted
                to integers. Negative values return 0.

        Returns:
            float: The CDF value for k, or 0 if k is out of range.
        """
    if not isinstance(k, int):
        k = int(k)

    if k < 0:
        return 0

    e = 2.7182818285
    cdf_value = 0

    for i in range(k + 1):
        e_neg_lambda = e ** (-self.lambtha)
        lambda_i = self.lambtha ** i

        i_factorial = 1
        for j in range(1, i + 1):
            i_factorial *= j

        cdf_value += (e_neg_lambda * lambda_i) / i_factorial

    return cdf_value
