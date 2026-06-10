#!/usr/bin/env python3
"""Module for Binomial distribution class."""


def factorial(n):
    """Return the factorial of n.

    Args:
        n (int): Non-negative integer.

    Returns:
        int: n!
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


class Binomial:
    """Represents a binomial distribution."""

    def __init__(self, data=None, n=1, p=0.5):
        """Initialize Binomial distribution.

        Args:
            data (list): Data to estimate the distribution from.
            n (int): Number of Bernoulli trials.
            p (float): Probability of a success.

        Raises:
            TypeError: If data is not a list.
            ValueError: If data has fewer than two points,
                        n is not positive, or p is invalid.
        """
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)

            p = 1 - (variance / mean)
            n = round(mean / p)
            p = mean / n

            self.n = n
            self.p = p

    def pmf(self, k):
        """Calculate the PMF for a given number of successes.

        Args:
            k (int): Number of successes.

        Returns:
            float: PMF value for k, or 0 if k is out of range.
        """
        k = int(k)

        if k < 0 or k > self.n:
            return 0

        coefficient = (factorial(self.n) //
                       (factorial(k) * factorial(self.n - k)))

        return coefficient * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    def cdf(self, k):
        """Calculate the CDF for a given number of successes.

        Args:
            k (int): Number of successes.

        Returns:
            float: CDF value for k, or 0 if k is out of range.
        """
        k = int(k)

        if k < 0 or k > self.n:
            return 0

        return sum(self.pmf(i) for i in range(k + 1))
