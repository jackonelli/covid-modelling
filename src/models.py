"""Models"""
import numpy as np


def nll_poiss(x, base, exp_):
    """Poisson NLL

    Evalute the negative log likelihood of Poisson,
    while ignoring constant terms.
    p(x; lambda_) = exp(-lambda_) lambda_^x/x!
    => - log p = lambda_ - x log lambda_ + log x!
    where the term log x! can be ignored.
    """

    num_days = len(x)
    lambda_ = base * exp_**np.arange(
        1, num_days + 1)  # Values of lambda as a function of day
    nll = np.sum(lambda_ - x**np.log(lambda_))
    return nll


def nll_gauss(x, base, exp_):
    """Gaussian NLL

    Evalute the negative log likelihood of Gaussian,
    while ignoring constant terms.
    """

    num_days = len(x)
    mu = base * exp_**np.arange(
        1, num_days + 1)  # Values of mu as a function of day
    nll = np.sum(np.log(mu) + x**2 / mu + mu)
    return nll


def param_search(model, cases: np.ndarray, a_0: float, b_0: float,
                 num_optim_runs: int, num_samples_per_optim):
    """Param search

    Start with initial guess for params a and b
    (the optimization is not sensitive to these).

    Randomly sample around this guess and improve it
    with params giving the lowest NLL

    Note: the current model is mu = a*b^i where i=1 on March 14.
    """
    nll_0 = model(cases, a_0, b_0)

    for _ in np.arange(num_optim_runs):
        a = 0.1 * np.random.rand(num_samples_per_optim, 1) + a_0
        b = b_0 + 0.01 * np.random.rand(num_samples_per_optim, 1)
        for (a_current, b_current) in zip(a, b):
            nll = model(cases, a_current, b_current)
            if nll < nll_0:
                nll_0 = nll
                a_0 = a_current
                b_0 = b_current
    return a_0, b_0


def generate_predictions(a_star, b_star, range_):
    """Gen predictions"""
    return a_star * b_star**np.arange(1, range_)
