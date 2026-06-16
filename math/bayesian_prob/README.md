# Bayesian Probability

Building Bayes' rule from scratch in Python/NumPy: likelihood, intersection, marginal probability, and posterior probability for a binomial trial.

## Background

A clinical trial gives `n` patients a drug, and `x` of them develop a side effect. The true probability `p` of developing the side effect is unknown. Instead of computing one single estimate of `p`, this project evaluates many *hypothetical* values of `p` at once and asks, for each one, two questions:

1. If this hypothesis were true, how likely is the data we actually observed? (**likelihood**)
2. Given the data we observed, how likely is this hypothesis to be true? (**posterior**)

The bridge between those two questions is Bayes' rule:

```
P(A | B) = P(B | A) · P(A) / P(B)
```

| Term | Name | Meaning here |
|---|---|---|
| `P(A)` | Prior | What we believed about `p` before seeing the data |
| `P(B \| A)` | Likelihood | How well a given `p` explains the observed `x` out of `n` |
| `P(B)` | Marginal | Overall probability of the data, averaged over all hypotheses |
| `P(A \| B)` | Posterior | Updated belief about `p` after seeing the data |

Each script below computes one term of that equation.

## Files

| File | Function | Computes |
|---|---|---|
| `0-likelihood.py` | `likelihood(x, n, P)` | `P(data \| p)` for each hypothetical `p` |
| `1-intersection.py` | `intersection(x, n, P, Pr)` | `P(data \| p) · P(p)` for each `p` |
| `2-marginal.py` | `marginal(x, n, P, Pr)` | `P(data)` — sum of all intersections |
| `3-posterior.py` | `posterior(x, n, P, Pr)` | `P(p \| data)` for each `p` |

Each function builds directly on the one before it — `posterior` is just `intersection / marginal`.

## Requirements

- Python 3 (pycodestyle compliant)
- `numpy`

## Usage

```python
import numpy as np
from posterior import posterior

# 11 hypothetical probabilities from 0.0 to 1.0
P = np.linspace(0, 1, 11)

# Uniform prior: no hypothesis favoured over another
Pr = np.ones(11) / 11

# 26 out of 130 patients had the side effect
result = posterior(26, 130, P, Pr)
print(result)
```

## How it works

### 1. Likelihood — `P(data | p)`

`x` follows a **binomial distribution**: given a fixed probability `p` and `n` trials, the chance of observing exactly `x` successes is

```
P(x | n, p) = C(n, x) · p^x · (1 − p)^(n − x)
```

`likelihood` evaluates this formula once for every value in `P`, returning an array of the same shape. A `p` that makes the observed `x` very plausible gets a high likelihood; a `p` that makes it implausible gets a likelihood near zero.

### 2. Intersection — `P(data ∩ p)`

```
intersection = likelihood(x, n, P) × Pr
```

Weighting the likelihood by the prior. If a hypothesis was already considered unlikely (`Pr` is small), even a high likelihood gets pulled down.

### 3. Marginal — `P(data)`

```
marginal = sum(intersection)
```

Adding up the intersection across every hypothesis gives the total probability of seeing this data at all, regardless of which `p` is true. This number does **not** depend on any single hypothesis — it's the normalizing constant in Bayes' rule.

### 4. Posterior — `P(p | data)`

```
posterior = intersection / marginal
```

Dividing each intersection by the marginal rescales the values so they sum to exactly 1 — turning them into a proper probability distribution over `p`. This is the updated belief: given the data observed, how plausible is each hypothetical `p`?

## Example

```bash
$ ./3-main.py
[0.00000000e+00 2.99729127e-03 9.63044824e-01 3.39513268e-02
 6.55839819e-06 1.26359684e-11 1.20692303e-19 6.74011797e-31
 1.05430721e-47 1.11125368e-77 0.00000000e+00]
```

With 26 out of 130 patients affected (≈20%), the posterior puts **96.3% of belief on p = 0.2**, the hypothesis closest to the observed rate — even though the prior treated all 11 hypotheses as equally likely going in.

## Validation rules (all four functions)

Checked in this exact order:

1. `n` must be a positive integer
2. `x` must be an integer ≥ 0
3. `x` cannot be greater than `n`
4. `P` must be a 1D `numpy.ndarray`
5. `Pr` must be a `numpy.ndarray` with the same shape as `P` *(intersection, marginal, posterior only)*
6. Every value in `P` must be in `[0, 1]`
7. Every value in `Pr` must be in `[0, 1]` *(intersection, marginal, posterior only)*
8. `Pr` must sum to 1, checked with `np.isclose` *(intersection, marginal, posterior only)*

## Author

KhadijaTheAnalyst — DLH AI Academy, Holberton ML curriculum