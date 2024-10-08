import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
customers_data = pd.read_csv("/content/Mall_Customers.csv")

# Display the shape and head of the dataset
print(customers_data.shape)
print(customers_data.head())

# Selecting the relevant data (columns 3 and 4)
data = customers_data.iloc[:, 3:5].values

# Plotting the dendrogram
import scipy.cluster.hierarchy as shc
plt.figure(figsize=(10, 7))
plt.title("Customer Dendograms")
dend = shc.dendrogram(shc.linkage(data, method='ward'))

# Applying Agglomerative Clustering
from sklearn.cluster import AgglomerativeClustering
cluster = AgglomerativeClustering(n_clusters=5, linkage='ward')
cluster.fit_predict(data)

# Plotting the clusters
plt.figure(figsize=(10, 7))
plt.scatter(data[:, 0], data[:, 1], c=cluster.labels_, cmap='rainbow')
plt.show()