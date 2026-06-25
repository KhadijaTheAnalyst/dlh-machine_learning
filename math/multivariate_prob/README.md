# Multivariate Probability

This module covers multivariate statistics and probability distributions, implemented from scratch in Python using NumPy.

---

## Files

| File | Description |
|------|-------------|
| `0-mean_cov.py` | Calculates the mean and covariance matrix of a dataset |
| `1-correlation.py` | Calculates a correlation matrix from a covariance matrix |
| `multinormal.py` | Class representing a Multivariate Normal distribution |

---

## Tasks

### 0. Mean and Covariance — `0-mean_cov.py`

```python
def mean_cov(X):
```

- `X`: `numpy.ndarray` of shape `(n, d)` — `n` data points, `d` dimensions
- Returns `mean` of shape `(1, d)` and `cov` of shape `(d, d)`
- Raises `TypeError` if `X` is not a 2D numpy array
- Raises `ValueError` if `n < 2`
- `numpy.cov` is not used

**Example:**
```python
np.random.seed(0)
X = np.random.multivariate_normal([12, 30, 10], [[36, -30, 15], [-30, 100, -20], [15, -20, 25]], 10000)
mean, cov = mean_cov(X)
print(mean)
# [[12.04341828 29.92870885 10.00515808]]
print(cov)
# [[ 36.2007391  -29.79405239  15.37992641]
#  [-29.79405239  97.77730626 -20.67970134]
#  [ 15.37992641 -20.67970134  24.93956823]]
```

---

### 1. Correlation — `1-correlation.py`

```python
def correlation(C):
```

- `C`: `numpy.ndarray` of shape `(d, d)` — a covariance matrix
- Returns a correlation matrix of shape `(d, d)`
- Each entry is defined as: **ρ<sub>ij</sub> = σ<sub>ij</sub> / (σ<sub>i</sub> σ<sub>j</sub>)**
- Raises `TypeError` if `C` is not a numpy array
- Raises `ValueError` if `C` is not a 2D square matrix

**Example:**
```python
C = np.array([[36, -30, 15], [-30, 100, -20], [15, -20, 25]])
Co = correlation(C)
print(Co)
# [[ 1.  -0.5  0.5]
#  [-0.5  1.  -0.4]
#  [ 0.5 -0.4  1. ]]
```

---

### 2. Initialize — `multinormal.py`

```python
class MultiNormal:
    def __init__(self, data):
```

- `data`: `numpy.ndarray` of shape `(d, n)` — `d` dimensions, `n` data points
- Sets public instance variables:
  - `mean`: shape `(d, 1)`
  - `cov`: shape `(d, d)`
- Raises `TypeError` if `data` is not a 2D numpy array
- Raises `ValueError` if `n < 2`
- `numpy.cov` is not used

---

### 3. PDF — `multinormal.py`

```python
def pdf(self, x):
```

Calculates the probability density function at a data point using the multivariate Gaussian formula:

$$f(x) = \frac{1}{\sqrt{(2\pi)^d |\Sigma|}} \exp\left(-\frac{1}{2}(x - \mu)^T \Sigma^{-1} (x - \mu)\right)$$

- `x`: `numpy.ndarray` of shape `(d, 1)`
- Returns the PDF value as a float
- Raises `TypeError` if `x` is not a numpy array
- Raises `ValueError` if `x` does not have shape `(d, 1)`

**Example:**
```python
np.random.seed(0)
data = np.random.multivariate_normal([12, 30, 10], [[36, -30, 15], [-30, 100, -20], [15, -20, 25]], 10000).T
mn = MultiNormal(data)
x = np.random.multivariate_normal([12, 30, 10], [[36, -30, 15], [-30, 100, -20], [15, -20, 25]], 1).T
print(mn.pdf(x))
# 0.00022930236202143827
```

---

## Requirements

- Python 3.5+
- NumPy
- `pycodestyle` compliant (version 2.5)

## Author

Khadija Mustafa — [KhadijaTheAnalyst](https://github.com/KhadijaTheAnalyst)