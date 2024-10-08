'''
Aim: Write a python program to implement the following geometric machine learning algorithm
1.   KNN
2.   Perceptron
3.   ANN using BackPropagation
4.   Linear and Logistic Regression
'''

############################# KNN #############################
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
iris = datasets.load_iris()
x = iris.data
y = iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(x_train, y_train)
accuracy = knn.score(x_test, y_test)
knn_pre = knn.predict(x_test)
cm = confusion_matrix(y_test, knn_pre)
print("Confusion Matrix")
print(cm)
print("Accuracy")
print(accuracy * 100)



############################# Perceptron #############################
import numpy as np
#define unitstep function
def unitStep(v1):
  if v1>=0:
    return 1
  else:
    return 0
def perceptronModel(x,w,b):
  v1 = np.dot(w,x)+b #dot func used for dot product bet. input param yunitStep(v1)
  y = unitStep(v1)
  return y
def OR_LogicFunction(x):
  w = np.array([1,1])
  b = -0.5
  return perceptronModel(x,w,b)
test1 = np.array([0,0])
test2 = np.array([0,1])
test3 = np.array([1,0])
test4 = np.array([1,1])
print("OR({},{})={}".format(0,0,OR_LogicFunction(test1)))
print("OR({},{})={}".format(0,1,OR_LogicFunction(test2)))
print("OR({},{})={}".format(1,0,OR_LogicFunction(test3)))
print("OR({},{})={}".format(1,1,OR_LogicFunction(test4)))

def unitStep(v2):
  if v2>=1:
    return 1
  else:
    return 0
def perceptronModel(x,w,b):
  v2 = np.dot(w,x)+b #dot func used for dot product bet. input param
  y = unitStep(v2)
  return y
def AND_LogicFunction(x):
  w = np.array([1,1])
  b = -0.5
  return perceptronModel(x,w,b)
print("AND({},{})={}".format(0,0,AND_LogicFunction(test1)))
print("AND({},{})={}".format(0,1,AND_LogicFunction(test2)))
print("AND({},{})={}".format(1,0,AND_LogicFunction(test3)))
print("AND({},{})={}".format(1,1,AND_LogicFunction(test4)))

def unitStep(v3):
  if v3>=1 or v3<=0:
    return 1

  else:
    return 0

def perceptronModel(x,w,b):
  v3 = np.dot(w,x)+b #dot func used for dot product bet. input param
  y = unitStep(v3)
  return y

def XOR_LogicFunction(x):
  w = np.array([-1,1])
  b = 0.5
  return perceptronModel(x,w,b)
# Print results
print("XOR({},{})={}".format(0, 0, XOR_LogicFunction(test1)))
print("XOR({},{})={}".format(0, 1, XOR_LogicFunction(test2)))
print("XOR({},{})={}".format(1, 0, XOR_LogicFunction(test3)))
print("XOR({},{})={}".format(1, 1, XOR_LogicFunction(test4)))



##################### ANN using BackPropagation #####################
import numpy as np

class NeuralNetwork:
  def __init__(self, input_size, hidden_size, output_size, learning_rate = 0.1):
    self.input_size = input_size
    self.hidden_size = hidden_size
    self.output_size = output_size
    self.learning_rate = learning_rate

    # Initialize Weights And Biases
    self.weights1 = np.random.randn(self.input_size, self.hidden_size) # Indented this line to be part of the __init__ method
    self.bias1 = np.zeros((1, self.hidden_size)) # Indented this line to be part of the __init__ method
    self.weights2 = np.random.randn(self.hidden_size, self.output_size) # Indented this line to be part of the __init__ method
    self.bias2 = np.zeros((1, self.output_size)) # Indented this line to be part of the __init__ method

  def sigmoid(self, x):
    return 1 / (1 + np.exp(-x))

  def sigmoid_derivative(self, x):
    return x * (1 - x)

  def forward(self, X):
    self.z1 = np.dot(X, self.weights1) + self.bias1
    self.a1 = self.sigmoid(self.z1)
    self.z2 = np.dot(self.a1, self.weights2) + self.bias2
    self.output = self.sigmoid(self.z2)
    return self.output

  def backward(self, X, y, output):
    self.error = y - output
    self.output_delta = self.error * self.sigmoid_derivative(output)
    self.a1_error = self.output_delta.dot(self.weights2.T)
    self.a1_delta = self.a1_error * self.sigmoid_derivative(self.a1)

    self.weights2 += self.a1.T.dot(self.output_delta) * self.learning_rate
    self.bias2 += np.sum(self.output_delta, axis=0, keepdims=True) * self.learning_rate
    self.weights1 += X.T.dot(self.a1_delta) * self.learning_rate
    self.bias1 += np.sum(self.a1_delta, axis=0, keepdims=True) * self.learning_rate # Fixed typo here: self.learning_ -> self.learning_rate

  def train(self, X, y, epochs=10000):
    for epoch in range(epochs):
      output = self.forward(X)
      self.backward(X, y, output)

  def predict(self, X):
    return self.forward(X)

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [0], [0], [1]])

nn = NeuralNetwork(input_size=2, hidden_size=2, output_size=1)
nn.train(X, y)

for x in X:
  print(f"Input: {x}, Predicted Output: {nn.predict(x)}")



################### Linear and Logistic Regression ###################

### 1. Linear Regression ###
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data_set = pd.read_csv("/content/Salary_Data.csv")
data_set.head()
x = data_set.iloc[:, :-1].values
y = data_set.iloc[:, 1].values
#print(x)
#print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1/3, random_state = 0)
r = LinearRegression()
r.fit(x_train, y_train)
#LinearRegression(copy_x = 2, fit_intercept = True, n_jobs = None, normalize = False)
y_pred = r.predict(x_test)
x_pred = r.predict(x_train)
plt.scatter(x_train, y_train, color = 'red')
plt.plot(x_train, x_pred, color = 'green')
plt.title('Salary vs Experience (Training Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
plt.scatter(x_test, y_test, color = 'red')
plt.plot(x_train, x_pred, color = 'green')
plt.title('Salary vs Experience (Testing Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

training_score = r.score(x_train, y_train)
testing_score = r.score(x_test, y_test)
print("Training Score: ", training_score)
print("Testing Score: ", testing_score)


### 2. Logistic Regression ###
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import seaborn as sns
import matplotlib.pyplot as plt
candidates={'gmat':[780,750,690,710,680,730,690,720,740,690,610,690,710,680,770,610,580,650,540,590,620,600,550,550,570,670,660,580,650,660,640,620,660,660,680,650,670,580,590,690],
            'gpa':[4,3.9,3.3,3.7,3.9,3.7,2.3,3.3,3.3,3.3,2.7,3.7,2.7,2.3,3.3,2.2,2.3,2.7,3,3.3,3.7,2.3,3.7,3.3,3,2.7,4,3.3,3.3,2.3,2.7,3.3,1.7,3.7,3.1,3.4,3.5,3.7,3.7,3.5],
            'work_experince':[3,4,3,5,4,6,1,4,5,1,3,5,6,4,3,1,4,6,2,3,2,1,4,1,2,6,4,2,6,5,1,2,4,6,5,1,2,1,4,5],
            'admitted':[1,1,0,1,0,1,0,1,1,0,0,1,1,0,1,0,0,1,0,0,1,0,0,0,0,1,1,0,1,1,0,0,1,1,1,0,0,0,0,1]}
df=pd.DataFrame(candidates,columns=['gmat','gpa','work_experince','admitted'])
print(df)
x=df[['gmat','gpa','work_experince']]
y=df['admitted']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=0)
lg=LogisticRegression()
lg.fit(x_train,y_train)
y_pred=lg.predict(x_test)
confusion_matrix=pd.crosstab(y_test,y_pred,rownames=['Actual'],colnames=['Predicted'])
sns.heatmap(confusion_matrix,annot=True)
plt.show()
print("Accuracy:", metrics.accuracy_score(y_test,y_pred))
print(y_pred)
print(y_test)
print(x_test)
print(x_train)
plt.show()