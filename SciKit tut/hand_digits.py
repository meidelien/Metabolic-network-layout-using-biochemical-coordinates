from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()
#split it in features and labels
X = iris.data
y = iris.target
classes = ['Iris Setosa', 'Iris Versicolour', 'Iris Virginica']

test = 5 + 5

# print(iris)
print(X.shape)
print(y.shape)

# Hours of studying vs good/bad grades
# 10 different students
# train a model with 8 students
# predict with the remaining 2
# level of accuruarcy of our model

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)



print("### THIS IS A PRINT TEST FOR STRING FORMATING {}".format(test))
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

model = svm.SVC()
model.fit(X_train, y_train)

print(model)

predictions = model.predict(X_test)
acc = accuracy_score(y_test, predictions)

for i in range(len(predictions)):
    print(classes[predictions[i]])