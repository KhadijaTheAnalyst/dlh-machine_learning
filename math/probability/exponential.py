#!/usr/bin/env python3
"""Module for the Exponential distribution class."""


class Exponential:
    """Represents an exponential distribution.

    The exponential distribution models the time between events in a
    Poisson process — i.e. events that occur continuously and independently
    at a constant average rate (lambda).

    Attributes:
        lambtha (float): The rate parameter — the expected number of
            occurrences in a given time frame.
    """

    def __init__(self, data=None, lambtha=1.):
        """Initializes an Exponential distribution.

        Args:
            data (list, optional): A list of data points used to estimate
                the distribution's lambda. Defaults to None.
            lambtha (float, optional): The rate parameter. Used only if
                data is None. Defaults to 1.0.

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
            # For exponential, lambda is the inverse of the sample mean
            self.lambtha = float(1 / (sum(data) / len(data)))

    def pdf(self, x):
        """Calculates the value of the PDF for a given time period.

        The Exponential PDF is defined as:
            f(x) = lambda * e^(-lambda * x)   for x >= 0

        Args:
            x (float): The time period. Negative values return 0.

        Returns:
            float: The PDF value for x, or 0 if x is out of range.
        """
        if x < 0:
            return 0

        e = 2.7182818285

        return self.lambtha * e ** (-self.lambtha * x)

    def cdf(self, x):
        """Calculates the value of the CDF for a given time period.

        The Exponential CDF is defined as:
            F(x) = 1 - e^(-lambda * x)   for x >= 0

        This represents the probability that the event occurs
        within time x.

        Args:
            x (float): The time period. Negative values return 0.

        Returns:
            float: The CDF value for x, or 0 if x is out of range.
        """
        if x < 0:
            return 0

        e = 2.7182818285

        return 1 - e ** (-self.lambtha * x)
