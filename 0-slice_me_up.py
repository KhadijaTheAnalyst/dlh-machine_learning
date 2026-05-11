#!/usr/bin/env python3
"""This script demonstrates how to slice an array in Python.
It creates an array of numbers and then slices it to obtain specific subsets of the array.
The first slice retrieves the first two numbers, the second slice retrieves the last five numbers,
and the third slice retrieves the 2nd through 6th numbers of the array. Finally,
it prints the results.
"""


arr = [9, 8, 2, 3, 9, 4, 1, 0, 3]
arr1 = arr[:2]
arr2 = arr[-5:]
arr3 = arr[1:6]
print("The first two numbers of the array are: {}".format(arr1))
print("The last five numbers of the array are: {}".format(arr2))
print("The 2nd through 6th numbers of the array are: {}".format(arr3))
