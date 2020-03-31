"""COVID-19 modelling"""
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from src import data
from src import visualize
from src import models


def main():
    """Main entry point for script"""
    filepath = "data/new_icu_cases_200329.xlsx"
    icu_data = data.IcuCases.from_excel(filepath)
    cases = icu_data.cases
    start_date = dt.date(2020, 3, 14)

    a_0 = 6
    b_0 = 1.3
    dates, cases = icu_data.filter_dates(data.after_date(start_date))
    a_star, b_star = models.param_search(models.nll_poiss, cases, a_0, b_0,
                                         100, 500)
    extrapolation_length = 3
    predictions = models.generate_predictions(
        a_star, b_star,
        len(cases) + extrapolation_length)

    visualize.plot_icu_cases(dates, cases, predictions)


if __name__ == "__main__":
    main()
