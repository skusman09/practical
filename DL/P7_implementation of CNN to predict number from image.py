from keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import matplotlib. pyplot as plt

(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

plt.imshow(X_train[2], cmap='gray')
plt.show()

print("Original shape:", X_train[0].shape)

X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

X_train = X_train.reshape(60000, 28, 28, 1)
X_test = X_test.reshape(10000, 28, 28, 1)

Y_train = to_categorical(Y_train, 10)
Y_test = to_categorical(Y_test, 10)

model = Sequential([
Conv2D(32, kernel_size=3, activation='relu', input_shape=(28, 28,1)),
MaxPooling2D(pool_size=(2, 2)),
Conv2D(64, kernel_size=3, activation='relu'),
MaxPooling2D(pool_size=(2,2)),
Flatten(),
Dense(128, activation='relu'),
Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, Y_train, validation_data=(X_test, Y_test), epochs=5, batch_size=64)

print(model.predict(X_test[:4]))
print(Y_test[:4])
plt.imshow(X_test[7])
plt.show()

loss ,accuracy = model.evaluate(X_test, Y_test)
print(f"Test accuracy: {accuracy * 100:.2f}%")