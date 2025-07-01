import cv2,numpy as np,matplotlib.pyplot as plt

img = cv2.imread('One-Piece-Anime-PNG-High-Quality-Image.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_, binary = cv2.threshold(gray,128,255,cv2.THRESH_BINARY_INV)
plt.imshow(binary)
plt.show()

no_l , l_i = cv2.connectedComponents(binary)

output = np.zeros_like(img)
colors = np.random.randint(0, 255, size=(no_l, 3))

for i in range(1,no_l):
    output[l_i == i] = colors[i]

plt.imshow(output)
plt.show()
