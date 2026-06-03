#!/usr/bin/env python3
"""Plot a stacked bar graph of fruit quantities per person."""
import numpy as np
import matplotlib.pyplot as plt


def bars():
    """Display a stacked bar chart showing fruit distribution."""
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))
    plt.figure(figsize=(6.4, 4.8))

    plt.ylim(0, 80)
    plt.yticks(np.arange(0, 81, 10))
    plt.title("Number of Fruit per Person")
    plt.ylabel("Quantity of Fruit")

    names = ["Farrah", "Fred", "Felicia"]
    colors = ['red', 'yellow', '#ff8000', '#ffe5b4']
    labels = ['apples', 'bananas', 'oranges', 'peaches']
    bottom = np.zeros(3)

    for i in range(len(fruit)):
        plt.bar(names, fruit[i], bottom=bottom,
                color=colors[i], label=labels[i], width=0.5)
        bottom += fruit[i]

    plt.legend()
    plt.show()
