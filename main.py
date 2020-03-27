"""COVID-19 modelling"""
from src import data
from src import visualize


def main():
    """Main entry point for script"""
    filepath = "data/new_icu_cases.xlsx"
    icu_data = data.IcuCases.from_excel(filepath)
    visualize.plot_cases(icu_data.days_to_ind(), icu_data.cases)


if __name__ == "__main__":
    main()
