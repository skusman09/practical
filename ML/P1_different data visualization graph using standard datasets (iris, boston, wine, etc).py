'''
Write a python program using matplotlib to demonstrate different data visualization graph using standard datasets (iris, boston, wine, etc)
1. Scatter plot
2. Box plot
3. Bar Chart
4. Line Chart
**NOTE: Run Each In Separate Code Box**
'''

#Main Code

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import datasets

dataset=datasets.load_iris()
iris=pd.DataFrame(dataset.data,columns=dataset.feature_names)
iris['species']=dataset.target
iris.head()
print(iris)


########## Scatterplot ###########
plt.figure()
plt.subplot(1,2,1),sns.scatterplot(x=iris['sepal length (cm)'] , y=iris['sepal width (cm)'],hue=iris['species'],palette=['red','green','orange'])
plt.subplot(1,2,2),sns.scatterplot(x=iris['petal length (cm)'] , y=iris['petal width (cm)'],hue=iris['species'],palette=['red','green','orange'])
plt.title('Comparision of different species wrt sepal length and sepal width')
print(" ")
print(" ")


########## Boxplot ###########
plt.figure()
plt.subplot(1,2,1),sns.boxplot(x=iris['species'],y=iris['sepal length (cm)'],orient='v',palette=['red','green','orange'])
plt.subplot(1,2,2),sns.boxplot(x=iris['species'],y=iris['sepal width (cm)'],orient='v',palette=['red','green','orange'])
plt.title('Sepal length distribution for different species')
plt.show()
plt.subplot(1,2,1),sns.boxplot(x=iris['species'],y=iris['petal length (cm)'],orient='v',palette=['red','green','orange'])
plt.subplot(1,2,2),sns.boxplot(x=iris['species'],y=iris['petal width (cm)'],orient='v',palette=['red','green','orange'])
plt.title('Petal length distribution for different species')
plt.show()


########## Barplot ###########
plt.figure(1)
plt.subplot(2, 2, 1)
plt.bar(iris['species'],iris['sepal_length'], color="green") # Changed column name to 'sepal_length'
plt.title('sepal length')
plt.subplot(2, 2, 2)
plt.bar(iris['species'],iris['sepal_width'], color="blue") # Changed column name to 'sepal_width'
plt.title('sepal width')
plt.subplot(2, 2, 3)
plt.bar(iris['species'],iris['petal_length'], color="red") # Changed column name to 'petal_length' 
plt.title('petal length')
plt.subplot(2, 2, 4)
plt.bar(iris['species'],iris['petal_width'], color="yellow") # Changed column name to 'petal_width'
plt.title('petal width')
plt.show()


########## Lineplot ###########
# Load iris dataset and convert to DataFrame
iris_dataset = load_iris()
iris = pd.DataFrame(data=iris_dataset['data'], columns=iris_dataset['feature_names'])

# Line Plot
plt.figure(1)
plt.plot(iris['sepal length (cm)'], color='blue', label='sepal length (cm)')
plt.plot(iris['sepal width (cm)'], color='red', label='sepal width (cm)')
plt.plot(iris['petal length (cm)'], color='yellow', label='petal length (cm)')
plt.plot(iris['petal width (cm)'], color='green', label='petal width (cm)')
plt.title('Line Plot')
plt.xlabel('Number of Samples')
plt.legend()
plt.show()