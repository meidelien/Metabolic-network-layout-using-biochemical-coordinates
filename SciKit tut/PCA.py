
import pandas as pd
import matplotlib
# matplotlib.use('tkagg')
#matplotlib.use('module')

import matplotlib.pyplot as plt

import sklearn
# from sklearn import datasets as datasets
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# iris = datasets.load_iris()

# dataset in pandas

df = pd.read_csv(url, names=['sepal length', 'sepal width', 'petal length', 'petal width', 'target'])

print(df)

features = ['sepal length', 'sepal width', 'petal length', 'petal width']  # Exact match feature names/columns when calling on them. Don't have any spaces

# Separating features from the dataframes.

x = df.loc[:, features].values

# Print pre-standardized feature values
print(x)

# Separating out the targets from the dataframe

y = df.loc[:, ['target']].values

# Standardizing feature values from x  = df.loc

x = StandardScaler().fit_transform(x)

print(x)

# Reducing dimensionality from the sepal len, sepal wid, petal len & petal wid to just two components
pca = PCA(n_components=2)

principalComponents = pca.fit_transform(x)

principalDf = pd.DataFrame(data=principalComponents, columns=['Principal component 1', 'Principal component 2'])

print(principalDf)

# principalDf = StandardScaler().fit_transform(principalDf)

# print(principalDf)


concatDf = pd.concat([principalDf, df[['target']]], axis=1)



viz = plt.figure(figsize=(8, 8))  # Sets dimensions of the figure
ax = viz.add_subplot(1, 1, 1)
ax.set_xlabel('Principal component 1', fontsize=15)
ax.set_ylabel('Principal component 2', fontsize=15)
ax.set_title('Two component PCA', fontsize=20)

targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = ['r', 'g', 'b']
for target, color in zip(targets, colors):
    indicesToKeep = concatDf['target'] == target
    ax.scatter(concatDf.loc[indicesToKeep, 'Principal component 1']
                 , concatDf.loc[indicesToKeep, 'Principal component 2']
                 , c=color
                 , s=50)
ax.legend(targets)
ax.grid()

# plt.plot(ax)
