'''
Aim: Write a python program to implement following Logistic ML Algorithm
1.   K-mean
2.   Decision Tree
3.   Hierarchical Clustering
'''

############### 1. K-mean ###############
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans

data = pd.read_csv("/content/housing.csv")
print(data.columns)
data = data.loc[:, ["median_income", "latitude", "longitude"]]
print(data.head())

kmeans = KMeans(n_clusters=6)
data["Cluster"] = kmeans.fit_predict(data)
data["Cluster"] = data["Cluster"].astype("int")
print(data.head())

plt.style.use("seaborn")
plt.rc("figure",autolayout = True)
plt.rc("axes", labelweight = "bold", labelsize = "large", titleweight = "bold", titlesize = 14, titlepad = 10)
sns.relplot(x = "longitude", y = "latitude", hue = "Cluster", data = data, height = 6)
plt.show()

############### 2. Decision Tree ###############
import numpy as np
from sklearn import linear_model, tree
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

dataset = load_iris()
X = dataset.data
Y = dataset.target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 50)

model = DecisionTreeClassifier().fit(X_train,Y_train)

# import StringIO from io instead of sklearn.externals.six
from io import StringIO
from IPython.display import Image
import pydot

dot_data = StringIO()
tree.export_graphviz(model, out_file=dot_data,
                     feature_names=dataset.feature_names,
                     class_names=dataset.target_names,
                     filled=True, rounded=True,
                     special_characters=True)

(graph,) = pydot.graph_from_dot_data(dot_data.getvalue())
graph.write_png('iris.png')
Image(graph.create_png())



########## 3.   Hierarchical Clustering ##########
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage
dataset = load_iris()
Y = dataset.target
X = pd.DataFrame(dataset.data)
X.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
link = linkage(X, method='ward')
plt.figure(figsize = (25,25))
plt.title("Iris Hierarchical Clustering-Dendrogram", size = 25)
plt.xlabel("Species", size = 25)
plt.ylabel("Cluster Distance", size = 25)
dendrogram(link)
plt.show()