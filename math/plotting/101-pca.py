#!/usr/bin/env python3
"""
Visualizes the Iris flower dataset in 3D using Principal
Component Analysis (PCA).
The 4-dimensional data is reduced to 3 principal components
and plotted
using a 3D scatter plot, with points colored by species
using the plasma colormap.
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Load the dataset from the numpy archive
lib = np.load("pca.zip")
data = lib["data"]       # shape (150, 4): flower measurements
labels = lib["labels"]   # shape (150,): species labels (0, 1, 2)

# Center the data by subtracting the mean of each feature
data_means = np.mean(data, axis=0)
norm_data = data - data_means

# Perform SVD to find the principal component directions
_, _, Vh = np.linalg.svd(norm_data)

# Project data onto the top 3 principal components (4D -> 3D)
pca_data = np.matmul(norm_data, Vh[:3].T)

# Extract the 3 dimensions for plotting
x = pca_data[:, 0]
y = pca_data[:, 1]
z = pca_data[:, 2]

# Create a 3D axes and configure the plot
ax = plt.axes(projection='3d')
ax.set_title("PCA of Iris Dataset")
ax.set_xlabel("U1")
ax.set_ylabel("U2")
ax.set_zlabel("U3")

# Scatter plot with points colored by species label
ax.scatter(x, y, z, c=labels, cmap="plasma")

plt.show()
