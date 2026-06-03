#!/usr/bin/env python3
"""
Line graph module
Plots y = x^3 as a red solid line with x ranging from 0 to 10
"""

import numpy as np
import matplotlib.pyplot as plt


def line():
    """
    Plots a line graph of y = x^3
    x ranges from 0 to 10
    """
    x = np.arange(0, 11)
    y = x ** 3

    plt.figure(figsize=(6.4, 4.8))
    plt.plot(x, y, color='red', ls='solid')
    plt.xlim(0, 10)
    plt.show()
