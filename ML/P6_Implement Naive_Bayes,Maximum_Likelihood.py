'''
WAP to implement following probabilistic Machine Learning Algorithms
1. Naive Bayes
2. Maximum Likelihood
'''

############### 1. Naive Bayes ###############
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn import datasets
from sklearn.metrics import confusion_matrix
iris = datasets.load_iris()
gnb = GaussianNB()
mnb = MultinomialNB()
y_pred_gnb = gnb.fit(iris.data, iris.target).predict(iris.data)
cnf_matrix_gnb = confusion_matrix(iris.target, y_pred_gnb)
print(cnf_matrix_gnb)
y_pred_mnb = mnb.fit(iris.data, iris.target).predict(iris.data)
cnf_matrix_mnb = confusion_matrix(iris.target, y_pred_mnb)
print(cnf_matrix_mnb)



############### 2. Maximum Likelihood ###############
from scipy import stats
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
np.random.seed(1)

#X-Axis for the plot
x_data = np.arange(-10,10,1)
print(x_data.shape)
#Y-Axis as the gaussian
y_data = stats.norm.pdf(x_data,0,3)

#Plot data
plt.plot(x_data, y_data)
plt.show()
plt.close()

def gaussian(params):
  x0 = params[0]
  sd = params[1]

  yPred = np.random.normal(x0, sd, size = 20)

  #calulate negative log likelihood
  LL = -np.sum(stats.norm.logpdf(y_data, loc = yPred, scale = sd))

  return(LL)

initParams = [1,1]

results = minimize(gaussian, initParams, method = 'Nelder-Mead')
print(results.x)

estParms = results.x
yOut = yPred = np.random.normal(estParms[0], estParms[1], size = 20)

plt.clf()
plt.plot(x_data, y_data, 'go')
plt.plot(x_data, yOut)
plt.show()