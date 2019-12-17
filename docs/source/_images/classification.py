import izzy as iz
from izviz.defaults import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Plotting theme
set_theme(theme='light', font_size=24)

"""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""
""" THE LOGISTIC FUNCTION """
"""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""

# Generate a number of x
x = np.linspace(0, 1, 100000).reshape(-1, 1)

# Compute logistic function
lr = iz.LogisticRegression(fit_intercept=True)
lr.fit(x, np.ravel(np.round(x)))
y = lr.predict_proba(x)[:, 1]
print(lr.coef_)

# Plot
plt.figure(figsize=(20, 10))
plt.plot(x, y)
plt.title('The Logistic Function')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('logistic_function.png')

""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""
""" LOGISTIC LIKELIHOOD FUNCTION """
""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""

# Generate a number of x and y, the true outcomes
x = np.linspace(0, 1, 100000).reshape(-1, 1)
y = np.ravel(np.round(x))

# To illustrate the joint probability function, do grid search of beta
beta = np.linspace(-2, 5, 500)

# Create model
lr = iz.LogisticRegression(fit_intercept=False)
lr.intercept_ = [0.]

# Compute log likelihood for all beta
log_likelihood = []
for b in beta:
    # Set beta
    lr.coef_ = np.array([[b]])

    # Compute log likelihood
    log_likelihood.append(lr.log_likelihood(x, y))

# Which beta has max log_likelihood?
df = pd.DataFrame({'beta': beta, 'log_likelihood': log_likelihood})
print(df.sort_values('log_likelihood', ascending=False).head(1))

# Fit to get real beta
lr.fit(x, y)

# Plot
plt.figure(figsize=(20, 10))
plt.plot(beta, log_likelihood)
plt.plot(np.repeat(lr.coef_[0][0], 2), [np.min(log_likelihood), np.max(log_likelihood)], 'k--')
plt.title('Maximum Log Likelihood Determines Coefficients')
plt.xlabel('potential coefficient value')
plt.ylabel('log likelihood')
plt.savefig('log_likelihood.png')
