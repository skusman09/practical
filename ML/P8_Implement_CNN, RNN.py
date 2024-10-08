'''
Aim: Write a python program to implement the following Deep Learning Algorithm
1.   CNN
2.   RNN
'''


################### 1.CNN ###################
import tensorflow as tf

# Define the CNN model
model = tf.keras.models.Sequential([
  tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
  tf.keras.layers.MaxPooling2D((2, 2)),
  tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
  tf.keras.layers.MaxPooling2D((2, 2)),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Load and preprocess the MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0
x_train = x_train.reshape((60000, 28, 28, 1))
x_test = x_test.reshape((10000, 28, 28, 1))

# Train the model
model.fit(x_train, y_train, epochs=5)

# Evaluate the model
loss, accuracy = model.evaluate(x_test, y_test)
print('Test accuracy:', accuracy)



################### 2.RNN ###################

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# Generate a random dataset
def generate_data(num_samples, seq_length, num_classes):
    # Generate random sequences
    X = np.random.rand(num_samples, seq_length, 1)  # Shape: (num_samples, seq_length, num_features)
    # Generate random labels
    y = np.random.randint(0, num_classes, num_samples)  # Random integers for class labels
    return X, y

# Parameters
num_samples = 1000
seq_length = 10
num_classes = 2  # Binary classification

# Create dataset
X, y = generate_data(num_samples, seq_length, num_classes)

# One-hot encode the labels
encoder = OneHotEncoder(sparse_output=False) # set sparse_output to False
y_onehot = encoder.fit_transform(y.reshape(-1, 1))

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_onehot, test_size=0.2, random_state=42)

# Build the RNN model
model = Sequential()
model.add(SimpleRNN(32, input_shape=(seq_length, 1), activation='tanh'))
model.add(Dense(num_classes, activation='softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test Accuracy: {accuracy:.4f}')