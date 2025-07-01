import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the segmented image (binary or labeled)
img = cv2.imread('download.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold if needed to create binary image
_, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

# Find connected components
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary)

# Copy the original image for annotation
output = img.copy()

# Label each region by its region number (starting from 1)
for i in range(1, num_labels):  # skip label 0 (background)
    x, y = centroids[i]
    label_number = str(i)
    cv2.putText(output, label_number, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)

# Display results
plt.figure(figsize=(10, 6))
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.title(f'Total Regions Found: {num_labels - 1}')
plt.axis('off')
plt.show()

