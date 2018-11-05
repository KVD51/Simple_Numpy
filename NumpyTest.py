import numpy as np
from matplotlib import pyplot as plt


marray = np.genfromtxt('NumpyTest.csv', delimiter=',', skip_header=1, dtype=int)

row_means = np.mean(marray, axis=1)
col_means = np.mean(marray, axis=0)

print(marray)
print('Row means', row_means)
print('Column means', col_means)


randNormal = np.random.normal(0.4, 1, size=10000)
randBinomial = np.random.binomial(100, 0.4, size=10000)

plt.hist(randNormal, bins=20, alpha=0.5)
plt.hist(randBinomial, bins=20, alpha=0.5)
plt.title('Histogram Examples Using Random Numbers')
plt.legend(['Random Normal', 'Random Binomial'])
plt.show()
