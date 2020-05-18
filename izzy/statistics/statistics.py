"""
statistics.py
written in Python3
author: C. Lockhart <chris@lockhartlab.org>
"""

import numpy as np


def histogram():
    """
    https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.histogram.html
    https://numpy.org/doc/1.18/reference/generated/numpy.histogram.html
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_histogram.html

    Returns
    -------

    """

    pass


def pmf(a, bins=10, cumulative=False):
    """
    Probability mass function.

    https://en.wikipedia.org/wiki/Probability_mass_function

    Parameters
    ----------
    a : ArrayLike
    bins : int or ArrayLike
    cumulative : bool

    Returns
    -------

    """

    values, edges = np.histogram(a, bins=bins)
    values /= len(a)
    if cumulative:
        values = np.cumsum(values)
    return values, edges


def pdf(a, bins=10):
    """
    Probability densitry function.

    https://en.wikipedia.org/wiki/Probability_density_function

    Parameters
    ----------
    a : ArrayLike
    bins : int or ArrayLike

    Returns
    -------

    """

    return np.histogram(a, bins=bins, density=True)


