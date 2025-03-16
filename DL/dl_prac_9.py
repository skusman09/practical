import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load and convert the image to RGB
image = cv2.imread('/content/bwimg.webp')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# Flipping operations
flipped_h = cv2.flip(image, 1) # Horizontal flip
flipped_v = cv2.flip(image, 0) # Vertical flip
# Rotation: Rotate 90 degrees
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated = cv2.warpAffine(image, rotation_matrix, (w, h))
# Translation: Shift by 50 pixels right and 30 pixels down
tx, ty = 50, 30
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
translated = cv2.warpAffine(image, translation_matrix, (w, h))
# Function to display images
def show_images(images, titles):
 plt.figure(figsize=(12, 8))
 for i, (img, title) in enumerate(zip(images, titles)):
    plt.subplot(2, 3, i + 1)
    plt.imshow(img)
    plt.title(title, fontsize=12)
 plt.axis('off')
 plt.tight_layout()
 plt.show()
# Image list and titles
images = [image, flipped_h, flipped_v, rotated, translated]
titles = ["Original Image", "Flipped Horizontally", "Flipped Vertically", "Rotated 90°",
"Translated"]
# Show the images
show_images(images, titles)

scaled = cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)

# Salt and Pepper Noise: Add random noise
def salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy_image = image.copy()
    total_pixels = image.size
    
    # Salt noise (white pixels)
    num_salt = int(salt_prob * total_pixels)
    salt_coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape]
    noisy_image[salt_coords[0], salt_coords[1], :] = 255

    # Pepper noise (black pixels)
    num_pepper = int(pepper_prob * total_pixels)
    pepper_coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape]
    noisy_image[pepper_coords[0], pepper_coords[1], :] = 0

    return noisy_image

# Apply salt and pepper noise
noisy_image = salt_and_pepper_noise(image, 0.01, 0.01)  # 1% salt and 1% pepper

# Function to display images
def show_images(images, titles):
    plt.figure(figsize=(14, 10))  # Adjust the figure size
    for i, (img, title) in enumerate(zip(images, titles)):
        plt.subplot(2, 4, i + 1)  # Update grid to 2 rows and 4 columns
        plt.imshow(img)
        plt.title(title, fontsize=12)
        plt.axis('off')
    plt.tight_layout()
    plt.show()

# Image list and titles
images = [scaled, noisy_image]
titles = ["Scaled 1.5x", "Salt and Pepper Noise"]

# Show the images
show_images(images, titles)
