# COVID-19 modelling

We intend to estimate a model to predict the number of visits to ICU
in Sweden, March-April, 2020.

The model assumes an exponential increase in the number of infected
individuals whereas the number of ICU patients is binomially distributed
with a small p value.

We approximate the binomially distribution as either Poisson or Gaussian
and then fit a model to the observed data.

Here is the data where the first element corresponds to March 14.
At the moment, March 27, the last data point is from March 26th.

## Get started

### Setup
Install required dependencies:

```bash
pip install -r requirements.txt
```

### Data
I haven't found a clean way of getting the data.
For now I manually download the excel from here:

https://portal.icuregswe.org/siri/report/vtfstart-corona

## Run
Currently, the script `main.py` only parses a local excel file and plots the data in a bar chart.

We will later move towards using notebooks for experiments and rather use the pure python code as a lib.
