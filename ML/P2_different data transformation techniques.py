'''
Prac 2: Write a python program to demonstrate the different data transformation techniques
1. Normalization
2. Various types of distribution
3. Scaling
4. Filtering

Writeups:
1. Data Transformations
2. Normalization
3. Feature Scaling
4. Filtering
5. Distribution
a. Bernoulli
b. Binomial
c. Poisson
d. Normal
'''

#Types of Distribution

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.stats import binom
from scipy.stats import poisson
from scipy.stats import norm
from scipy.stats import bernoulli

############## Bernoulli Distribution ##############
s = np.random.binomial(10,0.5,1000)
plt.hist(s,16,color = 'orange')
plt.title('Bernoulli Distribution')
plt.show()


############## Binomial Distribution ##############
data = binom.rvs(n=17,p=0.7,size=1000)
ax = sns.distplot(data, 16,color = 'orange', hist_kws={"linewidth":22,'alpha':0.65})
ax.set(xlabel='Binomial Distribution', ylabel='Frequency')
plt.title('Binomial Distribution')
plt.show()

################ Poisson Distribution ################
s = np.random.poisson(5,10000)
plt.hist(s,16,color = 'Magenta')
plt.title('Poisson Distribution')
plt.show()


################ Normal Distribution ################
data = norm.rvs(size=10000)
ax = sns.distplot(data, 16,color = 'orange', hist_kws={"linewidth":22,'alpha':0.65})
ax.set(xlabel='Normal Distribution', ylabel='Frequency')
plt.title('Normal Distribution')
plt.show()


################ Filtering ################
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df.head()
t1 = df.iloc[4,0]
print(t1)           #Display element on 1st column, 5th row of the dataset
t2 = df.iloc[:,2:5]
print(t2)           #Display elements from 3rd column to 5th column
t3 = df.iloc[1:3,:]
print(t3)           #Display elements from 2nd and 3rd row of all columns

t4 = df[df['sepal width (cm)'] < 3.5]
print(t4)       #Printing records from the dataset having sepal length less than sepal width < 3.5

t5 = df[(df['sepal length (cm)'] > 4.9) & (df['petal length (cm)'] <= 1.4)]
print(t5)       #Printing records from the dataset where sepal length > 4.9 and petal length <= 1.4


#################### Data Transformation ####################
from sklearn import preprocessing
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_diabetes
from sklearn.preprocessing import MinMaxScaler

diab = load_diabetes()
diab = pd.DataFrame(diab.data, columns=diab.feature_names)
print("Dataset")
print(diab.head())
scaled_data = MinMaxScaler(diab)
x = diab[['age','sex']]
scaler = MinMaxScaler()
scalerx = scaler.fit_transform(x)
print(scalerx)
scaledx = pd.DataFrame(data = scalerx, columns=['age','sex'])
print(scaledx)
