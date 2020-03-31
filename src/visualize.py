"""Visualize module"""
import matplotlib.pyplot as plt
from src import data


def plot_icu_cases(dates, cases, predictions):
    """Simple bar plot of cases per day"""
    plt.plot_date(dates, cases)
    extended_dates = data.extend_date_range(dates, len(predictions))
    plt.plot(extended_dates, predictions, '-.')
    plt.title("New ICU cases for COVID-19")
    plt.show()
