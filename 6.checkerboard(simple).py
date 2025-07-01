import cv2,numpy as np,matplotlib.pyplot as plt

img = cv2.imread('ches.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

found,corner = cv2.findChessboardCorners(gray,(7,7),None)
imgs = cv2.drawChessboardCorners(img,(7,7),corner,True)
plt.imshow(imgs) # only image
