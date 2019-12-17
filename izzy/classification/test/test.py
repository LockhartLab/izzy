
from izzy.datasets import random_dataset
from izzy.classification import confusion_matrix
import numpy as np
import pandas as pd
from scipy.sparse import coo_matrix
import time

# Create random dataset
df = random_dataset(n_columns=2, null_proportion=0.)
y_true = df[0].round()
y_pred = df[1].round()

# Confusion matrix
t0 = time.time()
cm = confusion_matrix(y_true, y_pred, needs_classify=False)
t1 = time.time()
print(t1 - t0, cm)

t0 = time.time()
n_classes = len(np.unique(y_true))
w = np.ones(len(y_true))
cm = coo_matrix((w, (y_true, y_pred)), shape=(n_classes, n_classes), dtype='int').toarray()
t1 = time.time()
print(t1 - t0, pd.DataFrame(cm, index=[0, 1], columns=[0, 1]))
