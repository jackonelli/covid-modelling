"""Data module"""
from typing import Optional, Union
from pathlib import Path
import datetime as dt
import pandas as pd
import numpy as np


class IcuCases():
    """New ICU cases per day"""
    def __init__(self, dates: np.ndarray, cases: np.ndarray):
        self.dates = dates
        self.cases = cases

    def days_to_ind(self):
        """Generates an array of indices from the country's reported days"""
        day_diff = self.dates - self.dates[0]
        return np.array([int(x / np.timedelta64(1, 'D')) for x in day_diff])

    def filter_dates(self, date_filter):
        """Filter on date condition.
        Return a subset of dates and cases
        based on some filter of the dates
        """
        inds = date_filter(self.dates)
        return (self.dates[inds], self.cases[inds])

    @staticmethod
    def from_excel(excelfile: Union[Path, str]) -> "IcuCases":
        """Init from excel file"""
        raw_data = _df_from_xls(excelfile)
        dates = raw_data["Datum"].values.astype("datetime64[D]")
        cases = raw_data["Antal vårdtillfällen"].values
        icu = IcuCases(dates, cases)
        return icu


def _df_from_xls(excelfile: Union[Path, str]) -> pd.DataFrame:
    """Read excel file into dataframe"""
    excelfile = Path(excelfile)
    if not excelfile.exists():
        raise FileNotFoundError("Excel file: '{}' not found".format(excelfile))

    # The excel sheet has one row with only one column named "Datum"
    # Then the actual headers appear on row two
    df = pd.read_excel(excelfile, skiprows=1, parse_dates=[0])
    return df


def _parse_date(date: str) -> dt.date:
    return dt.datetime.strptime(date, "%Y-%m-%d").date()


def after_date(date: dt.date):
    return lambda input_: input_ > date


def extend_date_range(dates: np.ndarray, desired_length: int):
    """Extrapolate a daterange based on """
    last_date = dates[-1]
    extended_dates = np.array([
        last_date + np.timedelta64(i, "D")
        for i in np.arange(1, desired_length - len(dates) + 1)
    ])
    return np.append(dates, extended_dates)
