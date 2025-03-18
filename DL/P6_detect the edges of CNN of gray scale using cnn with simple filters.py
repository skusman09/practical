import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import cv2

def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (128, 128))
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=(0, -1))
    return img

edge_filter = np.array([[[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]])
edge_filter = edge_filter.reshape((3, 3, 1, 1))

model = Sequential([
    Conv2D(1, kernel_size=(3, 3),
           padding='same',
           use_bias=False,
           input_shape=(128, 128, 1))
])

model.layers[0].set_weights([edge_filter])
model.layers[0].trainable = False

image_path = '/content/bwimg.jpg'
input_image = preprocess_image(image_path)
output_image = model.predict(input_image)

# Display the images
plt.figure(figsize=(10, 5))

# Original grayscale image
plt.subplot(1, 2, 1)
plt.title("Original Grayscale Image")
plt.imshow(input_image[0, :, :, 0], cmap='gray')

# Edge detection output
plt.subplot(1, 2, 2)
plt.title("Edge Detection Output")
plt.imshow(output_image[0, :, :, 0], cmap='gray')

plt.show()
