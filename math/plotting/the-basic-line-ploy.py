#!/usr/bin/python

import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plot
# plt.plot(x,y)

# Multiple lines on one plot
plt.plot(x, y, label='Line A')
plt.plot(x, [1, 3, 5, 7, 9], label='Line B')
plt.legend() # shows the labels

# Scatter plot (dots instead of line)
# plt.scatter(x, y, color ='red')

# Bar chart
# plt.bar(x, y, color='teal')

# Labels
plt.title("My First Plot")
plt.xlabel("X axis")
plt.ylabel("Y axis")

# To customize (colors, style, grid)
plt.plot(x, y, color ='purple', linewidth=2, linestyle='--', marker='o')
plt.grid(True)

# always use savefig before show
# Saving instead of showing
plt.savefig('my_first_plot.png', dpi=150) # saves as image file

# Show it
plt.show()
