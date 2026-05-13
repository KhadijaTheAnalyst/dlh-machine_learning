#!/usr/bin/env python3
""" This modules represents matrix multliplication"""

import numpy as np

def np_matmul(mat1, mat2):
    """Multiply two matrices, rows into column"""
    return np.matmul(mat1, mat2)  # return mat1 @ mat2
