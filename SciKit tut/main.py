from sklearn import datasets
import numpy as np

iris = datasets.load_iris()
# Split dateentries by features and labels

x = iris.data
y = iris.target