"""
transform.py
------------


"""

from izzy.misc import ArrayLike
from izzy.regression import sigmoid_fit

import numpy as np
import pandas as pd


# Clip
def clip(x, left=None, right=None, cut=False):
    """
    Clips an array

    If `cut` = False, this sets any values < `left` to `left` and values > `right` to `right`.
    If `cut` = True, then the values < `left` and values > `right` are removed.

    Parameters
    ----------
    x : ArrayLike
        Array to clip
    left : int or float
        Left boundary to clip or cut
    right : scalar
        Right boundary to clip or cut
    cut : bool
        Flag to determine if we should clip or cut

    Returns
    -------
    ArrayLike
        Clipped or cut array
    """

    # If cut = False, use numpy clip function
    if not cut:
        array = np.clip(x, a_min=left, a_max=right)

    # Otherwise, cut
    else:
        # If x is a list, tuple, or set, we have to convert to numpy array
        if isinstance(x, (list, tuple, set)):
            x = np.array(x)

        # We needed to convert to numpy for slicing by boolean array
        x = x[np.greater_equal(x, left) & np.less_equal(x, right)]

    # Return array
    return x


# Cube
def cube(x):
    """
    Raises to a power of 3

    Parameters
    ----------
    x : int, float, or ArrayLike

    Returns
    -------
    int, float, or ArrayLike
        Value(s) raised to power of 3
    """

    return power(x, exponent=3)


# Desigmoid
def desigmoid(x, y, a=None, n=None):
#     Get sigmoid optimized parameters
    if a is None or n is None:
        a, n = sigmoid_fit(x, y)

    # Return inverse of sigmoid
    return np.power((1. - x) / (a * x), 1. / n)


# Granulate
# TODO add ability to return bin numbers instead of actual elements
def granulate(x, bins=None, mode=None, retbins=False):
    """
    Transforms `x` into coarse bins

    Parameters
    ----------
    x : ArrayLike
       Array to granulate
    bins : int or ArrayLike
        If int, produce that many bins according to `mode`; otherwise, use bins
    mode : str
        Options include 'quantile', 'equal', 'left-equal', 'right-equal', 'binary', or 'distinct'. Note that 'equal'
        and 'left-equal' are synonyms. If mode = 'distinct', no transformation is performed. The mode = 'binary' is the
        same as 'distinct', except that we check that there are only two types of observations.
    retbins : bool
        Should the bins be returned?

    Returns
    -------
    ArrayLike or (ArrayLike, ArrayLike)
        Granulated array and (optional) bins
    """

    # Alias mode = 'equal' to 'left-equal'
    if mode == 'equal':
        mode = 'left-equal'

    # Minimum and maximum of array
    array_min = np.min(x)
    array_max = np.max(x)

    # Assign labels for equal bin sizes using numpy.digitize
    if mode in ('left-equal', 'right-equal'):
        # Is bins an integer? If so, we need to generate
        if isinstance(bins, np.int):
            # Create bins
            bins = np.linspace(start=array_min, stop=array_max, num=bins + 1)

            # If left-equal, set last bin to infinity. If right-equal, set first bin to -infinity.
            if mode == 'left-equal':
                bins[-1] = np.inf
            elif mode == 'right-equal':
                bins[0] = -np.inf

        # Are these bins right-aligned?
        right = False if mode == 'left-equal' else True

        # Transform array
        array = np.digitize(x, bins=bins, right=right)

    # Assign labels for quantiles
    elif mode == 'quantile':
        x, _ = pd.qcut(x=x, q=bins, labels=False, retbins=True, duplicates='drop')

    # If binary, check that there are only two types of observations
    elif mode == 'binary':
        assert len(np.unique(x)) == 2, 'expecting only two types of observations'

    # Return
    return x if not retbins else (x, bins)


# Natural logarithm
def ln(x):
    """
    Computes natural logarithm

    Parameters
    ----------
    x : int, float, or ArrayLike
        Value(s)

    Returns
    -------
    int, float, or ArrayLike
        Natural logarithm of `x`
    """

    return np.log(x)


# Logarithm for arbitrary base
def log(x, base=10):
    """
    Computes logarithm for an arbitrary base

    Parameters
    ----------
    x : int, float, or ArrayLike
        Value(s)
    base : int or float
        Logarithmic base

    Returns
    -------
    int, float, or ArrayLike
        Base `base` logarithm of `x`
    """

    return np.log(x) / np.log(base)


# Raise to arbitrary power
def power(x, exponent):
    """
    Raises to an arbitrary exponent

    Parameters
    ----------
    x : int, float, or ArrayLike
        Value(s)
    exponent : int or float
        Exponent

    Returns
    -------
    int, float, or ArrayLike
        Value(s) raised to `exponent`
    """

    return np.power(x, exponent)


# Square
def square(x):
    """
    Raises to a power of 2

    Parameters
    ----------
    x : int, float, or ArrayLike

    Returns
    -------
    int, float, or ArrayLike
        Value(s) raised to power of 2
    """

    return power(x, exponent=2)


# Compute the weight of evidence
# TODO does this belong here or in metrics?
def weight_of_evidence(y, total_miss, total_hit, hit_class=1., iv=False):
    """
    Computes the weight of evidence

    Parameters
    ----------
    y : ArrayLike
        True outcomes for subpopulation
    total_miss : int
        Sum of all "misses" in population
    total_hit : int
        Sum of all "hits" in population
    hit_class : int, float, str, or bool
        Positive outcome class label
    iv : bool
        Should we return weight of evidence or information value (IV)?

    Returns
    -------
    float
        weight of evidence
    """

    # Number of classes must be 2
    assert len(np.unique(y)) == 2

    # Compute sum of misses, sum of hits
    is_hit_class = np.equal(y, hit_class)
    sum_miss = np.sum(~is_hit_class)
    sum_hit = np.sum(is_hit_class)

    # Compute miss & hit proportions
    p_miss = sum_miss / total_miss
    p_hit = sum_hit / total_hit

    # Return weight of evidence
    f = 1. if not iv else (p_hit - p_miss)
    return f * ln(p_hit / p_miss)


# Do a weight of evidence transformation
def woeify(x, y, bins=10, mode='equal'):
    """
    Transforms x into weight of evidence

    Parameters
    ----------
    x
    y
    bins
    mode

    Returns
    -------

    """

    pass