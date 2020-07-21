
from izzy import granulate
from functools import partial
import pandas as pd


x = [1, 2, 3]
y = [4, 5, 1]

df = pd.DataFrame({'x': x, 'y': y})

function = partial(granulate, bins=2, mode='right-equal')

print(function(x, retbins=True))