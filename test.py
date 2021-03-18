import numpy as np
from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()
print(digits.data)

digits.target = np.array([0, 1, 2, 8, 9, 8])