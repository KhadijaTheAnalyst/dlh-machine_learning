#!/usr/bin/env python3
"""
Module that displays multiple plots in a single figure.

The figure contains:
- A cubic function plot
- A scatter plot of height vs weight
- An exponential decay plot (C-14)
- A comparison of radioactive decay curves
- A histogram of student grades
"""

import numpy as np
import matplotlib.pyplot as plt


def all_in_one():
    """
    Plots five different graphs in a single figure using a 3x2 grid layout.

    The plots include:
    - A cubic function (x^3)
    - A scatter plot of simulated human height vs weight
    - Exponential decay of C-14 (log scale on y-axis)
    - Comparison of decay between C-14 and Ra-226
    - Histogram of student grades with bins of size 10

    The last subplot spans two columns.
    All titles and axis labels are set to x-small font size.
    """

    # --- Cubic function ---
    x0 = np.arange(0, 11)
    y0 = x0 ** 3

    # --- Scatter plot ---
    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
    y1 += 180

    # --- C-14 decay ---
    x2 = np.arange(0, 28651, 5730)
    r = np.log(0.5)
    y2 = np.exp((r / 5730) * x2)

    # --- Radioactive elements ---
    x3 = np.arange(0, 21000, 1000)
    y31 = np.exp((r / 5730) * x3)
    y32 = np.exp((r / 1600) * x3)

    # --- Histogram ---
    student_grades = np.random.normal(68, 15, 50)

    plt.figure(figsize=(12, 8))

    # ---------------- subplot 1 ----------------
    plt.subplot(3, 2, 1)
    plt.plot(x0, y0, color='red', ls='solid')
    plt.xlim(0, 10)
    plt.title("Men's Height vs Weight", fontsize='x-small')
    plt.xlabel("Height (in)", fontsize='x-small')
    plt.ylabel("Weight (lbs)", fontsize='x-small')

    # ---------------- subplot 2 ----------------
    plt.subplot(3, 2, 2)
    plt.scatter(x1, y1, color='magenta', s=5)
    plt.title("Men's Height vs Weight", fontsize='x-small')
    plt.xlabel("Height (in)", fontsize='x-small')
    plt.ylabel("Weight (lbs)", fontsize='x-small')

    # ---------------- subplot 3 ----------------
    plt.subplot(3, 2, 3)
    plt.plot(x2, y2, color='blue')
    plt.yscale('log')
    plt.xlim(0, 28650)
    plt.title("Exponential Decay of C-14", fontsize='x-small')
    plt.xlabel("Time (years)", fontsize='x-small')
    plt.ylabel("Fraction Remaining", fontsize='x-small')

    # ---------------- subplot 4 ----------------
    plt.subplot(3, 2, 4)
    plt.plot(x3, y31, 'r--', label="C-14")
    plt.plot(x3, y32, 'g-', label="Ra-226")
    plt.legend(loc="upper right")
    plt.xlim(0, 20000)
    plt.ylim(0, 1)
    plt.title("Exponential Decay of Radioactive Elements", fontsize='x-small')
    plt.xlabel("Time (years)", fontsize='x-small')
    plt.ylabel("Fraction Remaining", fontsize='x-small')

    # ---------------- subplot 5 + 6 ----------------
    plt.subplot(3, 2, (5, 6))
    bins = np.arange(0, 101, 10)

    plt.hist(student_grades, bins=bins, edgecolor='black')
    plt.xlim(0, 100)
    plt.ylim(0, 30)

    plt.xticks(np.arange(0, 101, 10))
    plt.yticks(np.arange(0, 31, 5))

    plt.title("Project A", fontsize='x-small')
    plt.xlabel("Grades", fontsize='x-small')
    plt.ylabel("Number of Students", fontsize='x-small')

    # ---------------- global title ----------------
    plt.suptitle("All in One")

    plt.tight_layout()
    plt.show()
