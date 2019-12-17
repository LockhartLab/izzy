
from izzy.classification import classify, LogisticRegression

import numpy as np
import pandas as pd

# Number of samples
n = 100000

# Build DataFrame
df = pd.DataFrame({
    0: np.random.rand(n),
    1: np.random.rand(n),
    2: np.random.rand(n)
})

# Define input / output for modeling
x = df[[0, 1]]
y = np.array(df[2]*100/30., dtype='int')

# Build logistic regression
lr = LogisticRegression(multi_class='auto')
lr.fit(x, y)

# Classify according to internal classified and sklearn learn
y_class1 = classify(lr.predict_proba(x))
y_class2 = lr.predict(x)

# Ensure that classes match up
assert (y_class1 == y_class2).all()

