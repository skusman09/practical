import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

def generate_data(n_samples=1000, sequence_length=10):
    X = np.random.rand(n_samples, sequence_length, 1)
    y = np.sum(X, axis=1)
    return X, y

X_train, y_train = generate_data()
X_test, y_test = generate_data(200)

model = Sequential([
    SimpleRNN(50, activation='relu', input_shape=(10,1)), Dense(1)])

model.compile(optimizer='adam', loss='mse')

model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

sample_input = np.random.rand(1, 10, 1)
predicted_output = model.predict(sample_input)
print("Predicted sum:", predicted_output)