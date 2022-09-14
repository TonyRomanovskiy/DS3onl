# Netology.ru lesson1

from matplotlib import pyplot as plt

import seaborn as sns

from pylab import rcParams
rcParams['figure.figsize'] = (9,6)
import numpy as np


from sklearn import datasets

data = datasets.load_boston()

#print(data['DESCR'])

X, y = datasets.load_boston(return_X_y = True)

X.shape

y.shape
