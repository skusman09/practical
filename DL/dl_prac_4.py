import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
# XOR input and output
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
Y = np.array([[0], [1], [1], [0]])
# Model definition
model = Sequential()
model.add(Dense(2, input_dim=2, activation='relu'))
model.add(Dense(2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# Compile model
model.compile(optimizer='Adadelta', loss='binary_crossentropy', metrics=['accuracy'])
# Train the model
model.fit(X, Y, epochs=100, verbose=1)
# Print results
print('Expected:', [i[0] > 0 for i in Y])
print('Predicted:', [int(round(i[0])) for i in model.predict(X)])

