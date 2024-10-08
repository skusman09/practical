import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix

# Load dataset
dataset = pd.read_csv("/content/drive/MyDrive/College_Work/SEM-3/AAI/AAI Practical/AAI_P9/iris.csv")

# Split features and target variable
x = dataset.iloc[:, [0, 1, 2, 3]].values
y = dataset.iloc[:, 4].values

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)

# Feature scaling
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# Train the Logistic Regression model
classifier = LogisticRegression(random_state=0, solver='lbfgs', multi_class='auto')
classifier.fit(x_train, y_train)

# Predict on the test set
y_pred = classifier.predict(x_test)

# Compute confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Plot confusion matrix
plt.figure(figsize=(8, 6))
ax = plt.gca()
sns.heatmap(cm, annot=True, annot_kws={"size": 16}, fmt='d', cmap="Blues", ax=ax)
ax.set_title('Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()