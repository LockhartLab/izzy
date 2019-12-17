
from izzy.eda import fan1d, FeatureAnalyzer

import numpy as np

# Generate data
n = 1000000
x = np.random.rand(n)
z = np.random.rand(n)
y = np.round(np.random.rand(n))

# Create a FeatureAnalyzer
fan = FeatureAnalyzer(x=x, y=y, z=z, clean=False)

# Generate report
print(fan.performance()[0])

#
fan = fan1d(x=x, y=y)

print(fan.performance())

