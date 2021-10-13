from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score


iris = datasets.load_iris()
# Split data entries by features and labels

X = iris.data
y = iris.target

plt.plot(X, y)

