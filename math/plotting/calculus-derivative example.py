#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100) # 100 points from -5 to 5
y = x**2
dy = 2*x

plt.plot(x, y, label='f(x) = x**2')
plt.plot(x, dy, label ="f'(x) = 2x", linestyle='--')
plt.legend()
plt.title("Function and its Derivative")
plt.grid(True)
plt.show()
