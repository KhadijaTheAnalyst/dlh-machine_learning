# Advanced Linear Algebra Module

A Python package for performing advanced linear algebra operations on matrices, including determinant calculation, matrix inversion, cofactor expansion, and eigenvalue/eigenvector computation.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Module Documentation](#module-documentation)
- [Examples](#examples)
- [Complexity Analysis](#complexity-analysis)
- [Requirements](#requirements)
- [Testing](#testing)

## Overview

This module provides implementations of fundamental linear algebra operations from scratch. Each function is carefully documented and validated with proper error handling. Perfect for educational purposes and understanding how linear algebra algorithms work under the hood.

## Features

### Core Operations

- ✓ **Determinant Calculation** - Compute matrix determinants using cofactor expansion
- ✓ **Cofactor Calculation** - Calculate cofactors for use in other operations
- ✓ **Matrix Inverse** - Calculate inverse matrices (n×n)
- ✓ **Eigenvalues & Eigenvectors** - Find eigenvalues and corresponding eigenvectors
- ✓ **Input Validation** - Comprehensive error checking for all operations
- ✓ **Type Safety** - Clear exception types with descriptive messages

### Quality Features

- ✓ Optimized algorithms for small matrices
- ✓ Recursive implementations for larger matrices
- ✓ Complete docstrings following PEP 257
- ✓ Comprehensive test cases included
- ✓ Professional code documentation

## Project Structure

```
advanced_linear_algebra/
├── README.md                 # This file
├── 0-determinant.py         # Determinant calculation
├── 1-cofactor.py            # Cofactor matrix computation
├── 2-inverse.py             # Matrix inversion
├── 3-eigen.py               # Eigenvalue and eigenvector calculation
└── tests/                   # Test files (optional)
    ├── test_determinant.py
    ├── test_cofactor.py
    ├── test_inverse.py
    └── test_eigen.py
```

## Installation

1. Clone or download the repository:
```bash
git clone <repository_url>
cd advanced_linear_algebra
```

2. No external dependencies required (uses only Python standard library)

## Quick Start

```python
from determinant import determinant
from cofactor import cofactor
from inverse import inverse
from eigen import eigen

# Example 1: Calculate determinant
mat = [[1, 2], [3, 4]]
det = determinant(mat)
print(f"Determinant: {det}")  # Output: -2

# Example 2: Find cofactor matrix
cof = cofactor(mat)
print(f"Cofactor matrix: {cof}")

# Example 3: Calculate matrix inverse
inv = inverse(mat)
print(f"Inverse: {inv}")

# Example 4: Find eigenvalues and eigenvectors
eigenvalues, eigenvectors = eigen(mat)
print(f"Eigenvalues: {eigenvalues}")
print(f"Eigenvectors: {eigenvectors}")
```

## Module Documentation

### 1. Determinant (`0-determinant.py`)

Calculates the determinant of a square matrix.

**Function Signature:**
```python
def determinant(matrix: list) -> int or float
```

**Parameters:**
- `matrix` (list of lists): Square matrix

**Returns:**
- Determinant value

**Raises:**
- `TypeError`: If not a list of lists
- `ValueError`: If matrix is not square

**Algorithm:**
- 0×0 matrix: Returns 1
- 1×1 matrix: Returns the single element
- 2×2 matrix: Returns `(a·d) - (b·c)`
- n×n matrix (n > 2): Recursive cofactor expansion

**Time Complexity:** O(n!) for n×n matrix
**Space Complexity:** O(n²)

**Example:**
```python
mat = [[5, 7, 9], [3, 1, 8], [6, 2, 4]]
det = determinant(mat)  # Returns: 192
```

---

### 2. Cofactor (`1-cofactor.py`)

Calculates the cofactor matrix (matrix of cofactors).

**Function Signature:**
```python
def cofactor(matrix: list) -> list
```

**Parameters:**
- `matrix` (list of lists): Square matrix (minimum 2×2)

**Returns:**
- Cofactor matrix (same dimensions as input)

**Raises:**
- `TypeError`: If not a list of lists
- `ValueError`: If not square or if less than 2×2

**Algorithm:**
1. For each element (i, j) in the matrix:
   - Create a minor (remove row i and column j)
   - Calculate determinant of minor
   - Multiply by sign: (-1)^(i+j)
2. Return matrix of all cofactors

**Time Complexity:** O(n! · n²) for n×n matrix
**Space Complexity:** O(n²)

**Example:**
```python
mat = [[1, 2], [3, 4]]
cof = cofactor(mat)  # Returns: [[4, -3], [-2, 1]]
```

---

### 3. Inverse (`2-inverse.py`)

Calculates the inverse of a square matrix.

**Function Signature:**
```python
def inverse(matrix: list) -> list
```

**Parameters:**
- `matrix` (list of lists): Square matrix

**Returns:**
- Inverse matrix (same dimensions as input)

**Raises:**
- `TypeError`: If not a list of lists
- `ValueError`: If not square or if determinant is 0 (singular matrix)

**Algorithm:**
1. Calculate determinant (check if non-zero)
2. Calculate cofactor matrix
3. Transpose cofactor matrix (adjugate)
4. Divide each element by determinant

**Formula:** A⁻¹ = (1/det(A)) · adj(A)

**Time Complexity:** O(n!) for n×n matrix
**Space Complexity:** O(n²)

**Example:**
```python
mat = [[1, 2], [3, 4]]
inv = inverse(mat)  # Returns: [[-2.0, 1.0], [1.5, -0.5]]
```

---

### 4. Eigenvalues & Eigenvectors (`3-eigen.py`)

Calculates eigenvalues and eigenvectors of a matrix.

**Function Signature:**
```python
def eigen(matrix: list) -> tuple (list, list)
```

**Parameters:**
- `matrix` (list of lists): Square matrix

**Returns:**
- Tuple: (eigenvalues, eigenvectors)

**Raises:**
- `TypeError`: If not a list of lists
- `ValueError`: If not square

**Algorithm:**
1. Calculate characteristic polynomial: det(A - λI)
2. Find roots (eigenvalues)
3. For each eigenvalue, solve (A - λI)v = 0 for eigenvectors

**Time Complexity:** Varies by matrix size and eigenvalue-finding method
**Space Complexity:** O(n²)

**Example:**
```python
mat = [[1, 2], [3, 4]]
eigenvalues, eigenvectors = eigen(mat)
# eigenvalues: [5.372, -0.372]
# eigenvectors: [[-0.578], [-0.816]], ...
```

---

## Examples

### Example 1: Complete Matrix Analysis

```python
from determinant import determinant
from cofactor import cofactor
from inverse import inverse
from eigen import eigen

# Define a matrix
A = [[4, 7], [2, 6]]

# Step 1: Calculate determinant
det_A = determinant(A)
print(f"det(A) = {det_A}")  # 4

# Step 2: Calculate cofactor matrix
cof_A = cofactor(A)
print(f"Cofactor(A) = {cof_A}")  # [[6, -2], [-7, 4]]

# Step 3: Calculate inverse
if det_A != 0:
    inv_A = inverse(A)
    print(f"A⁻¹ = {inv_A}")
else:
    print("Matrix is singular (not invertible)")

# Step 4: Find eigenvalues and eigenvectors
eigenvalues, eigenvectors = eigen(A)
print(f"Eigenvalues: {eigenvalues}")
print(f"Eigenvectors: {eigenvectors}")

# Verify: A·v = λ·v (eigenvalue equation)
```

### Example 2: 3×3 Matrix Operations

```python
B = [[5, 7, 9], [3, 1, 8], [6, 2, 4]]

det_B = determinant(B)  # 192
cof_B = cofactor(B)     # 3×3 cofactor matrix
inv_B = inverse(B)      # 3×3 inverse matrix
eigenvalues, eigenvectors = eigen(B)
```

### Example 3: Error Handling

```python
# Not a square matrix
try:
    determinant([[1, 2, 3], [4, 5, 6]])
except ValueError as e:
    print(e)  # "matrix must be a square matrix"

# Singular matrix (determinant = 0)
try:
    inverse([[1, 1], [1, 1]])
except ValueError as e:
    print(e)  # "matrix is singular and cannot be inverted"

# Not a list of lists
try:
    determinant([1, 2, 3])
except TypeError as e:
    print(e)  # "matrix must be a list of lists"
```

## Complexity Analysis

| Operation | Time Complexity | Space Complexity | Notes |
|-----------|-----------------|------------------|-------|
| Determinant (n×n) | O(n!) | O(n²) | Exponential due to recursion |
| Cofactor (n×n) | O(n! · n²) | O(n²) | n² cofactors, each O(n!) |
| Inverse (n×n) | O(n! · n²) | O(n²) | Uses determinant + cofactor |
| Eigenvalues (n×n) | Varies | O(n²) | Depends on method used |

**Note:** These implementations prioritize clarity and correctness over performance. For large matrices (n > 10), use optimized libraries like NumPy or SciPy.

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Testing

Each module includes test cases. Run them individually:

```bash
# Test determinant
python3 0-determinant.py

# Test cofactor
python3 1-cofactor.py

# Test inverse
python3 2-inverse.py

# Test eigenvalues/eigenvectors
python3 3-eigen.py
```

Or run all tests at once:

```bash
python3 -m pytest tests/
```

## Common Patterns

### Check if matrix is invertible
```python
from determinant import determinant

mat = [[1, 2], [3, 4]]
if determinant(mat) != 0:
    print("Matrix is invertible")
else:
    print("Matrix is singular")
```

### Verify eigenvalue equation
```python
from eigen import eigen

eigenvalues, eigenvectors = eigen(A)
# For each eigenvalue λ and eigenvector v:
# A·v should equal λ·v
```

### Chain operations
```python
# Determinant of inverse = 1/determinant of original
det_A = determinant(A)
A_inv = inverse(A)
det_A_inv = determinant(A_inv)
assert det_A_inv ≈ 1/det_A
```

## Limitations & Future Improvements

- ✗ No support for complex numbers (eigenvalues)
- ✗ No optimization for sparse matrices
- ✗ No support for non-square matrices
- Future: Add matrix decomposition (LU, QR, SVD)
- Future: Add support for complex numbers
- Future: Optimize for large matrices

## References

- [Linear Algebra](https://en.wikipedia.org/wiki/Linear_algebra)
- [Determinant](https://en.wikipedia.org/wiki/Determinant)
- [Matrix Inverse](https://en.wikipedia.org/wiki/Invertible_matrix)
- [Eigenvalues and Eigenvectors](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors)

## Author

Created as part of the ALX/Holberton School advanced linear algebra curriculum.

## License

This code is provided for educational purposes.

## Support

For issues or questions, refer to the individual module documentation or contact the development team.