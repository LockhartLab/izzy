
from izzy.datasets import random_dataset
from izzy.classification import LogisticRegression
import numpy as np
import statsmodels.discrete.discrete_model as sm


def test_binomial():
    # Create random dataset
    df = random_dataset(n_columns=5, null_proportion=0.)
    x = df[[1, 2, 3, 4]]
    y = df[0].round()

    # Logistic Regression
    lr = LogisticRegression(fit_intercept=False)
    lr.fit(x, y)

    # Compute standard errors and compare
    ste1 = lr.standard_errors(x, y, mode='statsmodels')
    ste2 = lr.standard_errors(x, y, mode='R')
    ste3 = sm.Logit(y, x).fit().bse
    assert np.max(np.abs(ste1 - ste2)) < 1e-7
    assert np.max(np.abs(ste1 - ste3)) < 1e-7


def test_multinomial():
    # Create random dataset
    df = random_dataset(n_columns=5, null_proportion=0.)
    x = df[[1, 2, 3, 4]].values
    y = np.array(df[0] / 0.3, dtype='int')

    # Logistic regression
    lr = LogisticRegression(fit_intercept=False)
    lr.fit(x, y)

    # Compute standard errors
    ste = sm.MNLogit(y, x)
    print(ste.hessian(x))


test_multinomial()


