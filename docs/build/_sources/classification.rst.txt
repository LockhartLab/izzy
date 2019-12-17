Classification
==============

The goal of classification algorithms is to label data. Traditionally, this is
done by training the algorithm on historic data with known labels. 

Generic
-------

These are functions, metrics, and plots that pertain to all classification
algorithms.

Metrics
~~~~~~~

These are metrics for assessing the performance of classification algorithms.

.. currentmodule:: izzy.classification.metrics

.. autosummary::

   accuracy
   aic
   bic
   confusion_matrix
   f1
   gini
   ks
   performance_report
   precision
   recall
   roc

Plots
~~~~~

Plots specific to classification problems.

roc

Class
~~~~~

.. currentmodule:: izzy.classification.generic

.. autosummary::

   GenericModel

Logistic Regression
-------------------

Logistic regression is a classification algorithm that solves for the function
:math:`y(x) = \frac{1}{1+e^{-\beta x}}`, where :math:`y` is the outcome,
:math:`\beta` is a set of coefficients, and :math:`x` are predictor variables.

An example of the function :math:`y(x)` is presented below. Note that this
function is particularly suited for classification, since two states,
:math:`y(x) = 0` and :math:`y(x) = 1` are separated by a sharp transition, the
decision boundary.

.. image:: _images/logistic_function.png
   :width: 100%

Fitting the Model
~~~~~~~~~~~~~~~~~
The coefficients :math:`\beta` are chosen such that the log likelihood is
maximized. The likelihood function is the joint probability distribution of
coefficients :math:`\beta` with each outcome. Intuitively, the maximization of
this function is equivalent to saying that we want to choose :math:`\beta` such
that the predicted probability of success is highest when samples are actually
successfully **and** the predicted probability of failure is highest when samples
are actually failures. 

For the case where we have a logistic function with only 1 variable (and no
intercept), we can visualize the coefficient versus the log likelihood on a 2D
plane. The maximum of the function, as depicted with the dashed black line, is 
the most suitable for the modeled data.

.. image:: _images/log_likelihood.png
   :width: 100%

Although it looks easy to identify the coefficients from maximum log likelihood
as above, in practice the number of predictive variables can be high leading to
a complicated likelihood function. Therefore, the best bet is to use
optimization algorithms to solve for the coefficients.

Note that the cost function :math:`J = \frac{1}{2}(y - \hat{y})^2`, where
:math:`y` is the predicted outcome and :math:`\hat{y}` is the true outcome,
presents an equivalent way of expressing how coefficients :math:`\beta` are
selected. 

Class
~~~~~
.. currentmodule:: izzy.classification.logistic

.. autosummary::

   LogisticRegression

Random Forest
-------------

Class
~~~~~

.. currentmodule:: izzy.classification.tree

.. autosummary::
   
   RandomForest

