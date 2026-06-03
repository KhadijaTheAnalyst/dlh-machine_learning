#!/usr/bin/env python3
"""
Gradient Plot Module
Creates a scatter plot of sampled mountain elevations.
"""

import numpy as np
import matplotlib.pyplot as plt


def gradient():
    """Plots a scatter graph of mountain elevation with color mapping."""

    np.random.seed(5)

    x = np.random.randn(2000) * 10
    y = np.random.randn(2000) * 10

    # elevation model
    z = np.random.rand(2000) + 40 - np.sqrt(x**2 + y**2)

    plt.figure(figsize=(6.4, 4.8))

    scatter = plt.scatter(x, y, c=z, cmap="viridis")

    plt.title("Mountain Elevation")
    plt.xlabel("x coordinate (m)")
    plt.ylabel("y coordinate (m)")

    cbar = plt.colorbar(scatter)
    cbar.set_label("elevation (m)")

    plt.show()
