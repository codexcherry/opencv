
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
opp = [
    ('orginal',img1),
    ('HSV',cv2.cvtColor(img1,cv2.COLOR_RGB2HSV)),
    ('LAB',cv2.cvtColor(img1,cv2.COLOR_RGB2LAB)),
    ('HLS',cv2.cvtColor(img1,cv2.COLOR_RGB2HLS)),
    ('YCBCR',cv2.cvtColor(img1,cv2.COLOR_RGB2YCR_CB)),
    ('XYZ',cv2.cvtColor(img1,cv2.COLOR_RGB2XYZ))
]
plt.figure(figsize=(14, 10))
for i, (title, image) in enumerate(opp):
    plt.subplot(3, 2, i+1)  # 2 rows, 2 columns grid
    plt.imshow(image)
    plt.title(title)
plt.show()
