#sigmoid
import matplotlib.pyplot as plt
import numpy as np
def sigmoid(x):
    return 1/(1 + np.exp(-x))
x = np.linspace(-10,10, 100)
y = sigmoid(x)
print("Input:", -2)
print("Sigmoid Output:", sigmoid(-2))
plt.plot(x,y, label="sigmoid function")
plt.title("Sigmoid activation function")
plt.xlabel("Input(x)")
plt.ylabel("output (f(x))")
plt.legend()
plt.grid()
plt.show()

#tanh
import matplotlib.pyplot as plt
import numpy as np
def tanh(x):
  return np.tanh(x)
x = np.linspace(-10,10, 100)
y = tanh(x)
print("Input:", -2)
print("Sigmoid Output:", tanh(-2))
plt.plot(x,y, label="Tanh function")
plt.title("Tanh activation function")
plt.xlabel("Input(x)")
plt.ylabel("output (f(x))")
plt.legend()
plt.grid()
plt.show()

#relu
import matplotlib.pyplot as plt
import numpy as np
def relu(x):
  return np.maximum(0, x)
inputs = np.array([-2.0, -1.0, 0.0, 1.0, 2.0])
outputs = relu(inputs)
print("Input:", inputs)
print("ReLu Output:", outputs)

#example
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
model = Sequential([
Dense(64, activation='relu', input_dim=10),
Dense(32, activation='relu'),
Dense(1)
])

model.summary()