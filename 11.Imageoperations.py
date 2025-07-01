import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('image.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply binary thresholding
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# Find connected components
num_labels, labels_im = cv2.connectedComponents(binary)

# Generate a color image for labels
output = np.zeros_like(image)

for i in range(1, num_labels):
    output[labels_im == i] = colors[i]

plt.imshow(image)
plt.show()

plt.imshow(binary)
plt.show()

plt.imshow(output)
plt.show()
