# Probability

## Description

This module implements probability distribution classes from scratch, without relying on external statistics libraries. Each distribution is built using only core Python and NumPy for data handling, with mathematical constants and operations computed manually.

This project is part of the **Holberton School Machine Learning** curriculum, focusing on foundational understanding of probability distributions used in machine learning and statistics.

---

## Learning Objectives

By the end of this project, you should be able to explain:

- What a probability distribution is
- What a probability mass function (PMF) is
- What a probability density function (PDF) is
- What a cumulative distribution function (CDF) is
- What a percentile / quantile is
- What mean, variance, and standard deviation represent
- The characteristics of the Poisson, Exponential, Normal, and Binomial distributions

---

## Requirements

- Python 3.5+
- NumPy (for data generation in tests only)
- All files must be executable
- Code must follow `pycodestyle` (version 2.5)
- No external statistics or scipy libraries allowed

---

## File Structure

```
probability/
├── README.md
├── poisson.py          # Poisson distribution
├── exponential.py      # Exponential distribution
├── normal.py           # Normal distribution
└── binomial.py         # Binomial distribution
```

---

## Distributions

### Poisson — `poisson.py`

Models the number of events occurring in a fixed interval, given a known average rate (λ).

**Class:** `Poisson(data=None, lambtha=1.)`

| Method | Description |
|--------|-------------|
| `pmf(k)` | Probability Mass Function — P(X = k) |
| `cdf(k)` | Cumulative Distribution Function — P(X ≤ k) |

**PMF formula:**

```
P(X = k) = (e^(-λ) * λ^k) / k!
```

**Example:**
```python
import numpy as np
Poisson = __import__('poisson').Poisson

np.random.seed(0)
data = np.random.poisson(5., 100).tolist()

p1 = Poisson(data)
print('P(9):', p1.pmf(9))   # 0.03175849616802446

p2 = Poisson(lambtha=5)
print('P(9):', p2.pmf(9))   # 0.036265577412911795
```

---

### Exponential — `exponential.py`

Models the time between events in a Poisson process.

**Class:** `Exponential(data=None, lambtha=1.)`

| Method | Description |
|--------|-------------|
| `pdf(x)` | Probability Density Function — f(x) |
| `cdf(x)` | Cumulative Distribution Function — F(x) |

**PDF formula:**

```
f(x) = λ * e^(-λx)   for x ≥ 0
```

---

### Normal — `normal.py`

The Gaussian (bell curve) distribution, fundamental to statistics and machine learning.

**Class:** `Normal(data=None, mean=0., stddev=1.)`

| Method | Description |
|--------|-------------|
| `z_score(x)` | Calculates the z-score of a given x value |
| `x_value(z)` | Calculates the x value for a given z-score |
| `pdf(x)` | Probability Density Function — f(x) |
| `cdf(x)` | Cumulative Distribution Function — F(x) |

**PDF formula:**

```
f(x) = (1 / (σ√(2π))) * e^(-(x - μ)² / (2σ²))
```

---

### Binomial — `binomial.py`

Models the number of successes in a fixed number of independent Bernoulli trials.

**Class:** `Binomial(data=None, n=1, p=0.5)`

| Method | Description |
|--------|-------------|
| `pmf(k)` | Probability Mass Function — P(X = k) |
| `cdf(k)` | Cumulative Distribution Function — P(X ≤ k) |

**PMF formula:**

```
P(X = k) = C(n, k) * p^k * (1 - p)^(n - k)
```

where `C(n, k) = n! / (k! * (n - k)!)`

---

## Usage

All classes can be instantiated either from raw data or by providing distribution parameters directly.

```python
# From data
import numpy as np
data = np.random.poisson(5., 100).tolist()
p = Poisson(data)

# From parameters
p = Poisson(lambtha=5)
```

**Error handling:**

```python
Poisson(lambtha=-1)     # ValueError: lambtha must be a positive value
Poisson(data="hello")   # TypeError: data must be a list
Poisson(data=[1])       # ValueError: data must contain multiple values
```

---

## Author

**Khadija** — Civil Engineer turned Data Analyst & ML Engineer  
[GitHub](https://github.com/KhadijaTheAnalyst) · [Portfolio](https://khadijatheanalyst.github.io)

---

## License

This project is part of the Holberton School curriculum. All work is original and intended for educational purposes.