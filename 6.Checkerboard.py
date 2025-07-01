import cv2,numpy as np,matplotlib.pyplot as plt

img = cv2.imread('ches.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

found , corners = cv2.findChessboardCorners(gray,(7,7),None)

if found:
    obj = np.zeros((49,3),np.float32)
    obj[:,:2] = np.mgrid[0:7,0:7].T.reshape(-1,2)

    _,m,d,r,t = cv2.calibrateCamera([obj],[corners],gray.shape[::-1],None,None)

    proj,_ = cv2.projectPoints(obj,r[0],t[0],m,d)

    e = cv2.norm(corners,proj) / len(proj)

    print("Camera Matrix:\n", m)
    print("Distortion Coefficients:\n", d)
    print("Reprojection Error:", e)

    img = cv2.drawChessboardCorners(img,(7,7),corners,True)
    plt.imshow(img)
