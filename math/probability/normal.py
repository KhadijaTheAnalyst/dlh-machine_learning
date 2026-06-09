#!/usr/bin/env python3
"""Module for the Normal distribution class."""


class Normal:
    """Represents a normal (Gaussian) distribution.

    The normal distribution is a continuous probability distribution
    that is symmetric around its mean, forming the characteristic
    bell curve. It is defined by two parameters: the mean (μ) and
    the standard deviation (σ).

    Attributes:
        mean (float): The mean (μ) — center of the distribution.
        stddev (float): The standard deviation (σ) — spread of the
            distribution.
    """

    def __init__(self, data=None, mean=0., stddev=1.):
        """Initializes a Normal distribution.

        Args:
            data (list, optional): A list of data points used to estimate
                the distribution's mean and stddev. Defaults to None.
            mean (float, optional): The mean of the distribution. Used only
                if data is None. Defaults to 0.0.
            stddev (float, optional): The standard deviation. Used only if
                data is None. Defaults to 1.0.

        Raises:
            ValueError: If stddev is not a positive value.
            TypeError: If data is not a list.
            ValueError: If data does not contain multiple values.
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            self.mean = float(sum(data) / len(data))

            # Population variance: average of squared differences from the mean
            variance = sum((x - self.mean) ** 2 for x in data) / len(data)
            # Standard deviation is the square root of variance
            self.stddev = float(variance ** 0.5)

    def z_score(self, x):
        """Calculates the z-score of a given x value.

        The z-score measures how many standard deviations x is
        away from the mean:
            z = (x - μ) / σ

        Args:
            x (float): The data point to evaluate.

        Returns:
            float: The z-score of x.
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculates the x value for a given z-score.

        Inverse of the z-score formula:
            x = μ + z * σ

        Args:
            z (float): The z-score to evaluate.

        Returns:
            float: The x value corresponding to z.
        """
        return self.mean + z * self.stddev

    def pdf(self, x):
        """Calculates the value of the PDF for a given x value.

        The Normal PDF is defined as:
            f(x) = (1 / (σ * sqrt(2π))) * e^(-0.5 * ((x - μ) / σ)²)

        Args:
            x (float): The x value to evaluate.

        Returns:
            float: The PDF value for x.
        """
        e = 2.7182818285
        pi = 3.1415926536

        coefficient = 1 / (self.stddev * (2 * pi) ** 0.5)
        exponent = e ** (-0.5 * ((x - self.mean) / self.stddev) ** 2)

        return coefficient * exponent

    def cdf(self, x):
        """Calculates the value of the CDF for a given x value.

        The Normal CDF is approximated using the error function (erf):
            F(x) = 0.5 * (1 + erf((x - μ) / (σ * sqrt(2))))

        Args:
            x (float): The x value to evaluate.

        Returns:
            float: The CDF value for x.
        """
        pi = 3.1415926536

        # Normalize x to standard normal
        z = (x - self.mean) / (self.stddev * (2 ** 0.5))

        # Approximate erf using the Taylor series expansion
        erf = (2 / pi ** 0.5) * (
            z - (z ** 3) / 3 + (z ** 5) / 10 -
            (z ** 7) / 42 + (z ** 9) / 216
        )

        return 0.5 * (1 + erf)
