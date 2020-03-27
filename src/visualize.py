"""Visualize module"""
import matplotlib.pyplot as plt


def plot_cases(x, y):
    """Simple bar plot of cases per day"""
    plt.bar(x, y)
    plt.show()
