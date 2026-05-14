#!/usr/bin/env python3

import numpy as np

def add_matrices(mat1, mat2):

    arr1 = np.array(mat1)
    arr2 = np.array(mat2)

    if arr1.shape != arr2.shape:
        return None

    return (arr1 + arr2).tolist()
