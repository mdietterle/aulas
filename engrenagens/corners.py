import cv2
import numpy as np

img=cv2.imread('C:\\Users\\Martim\\OneDrive\\Scripts Python\\engrenagens\\engrenagem1.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
#cantos afiados
#dst = cv2.cornerHarris(gray,4,5,0.04)
#canntos arredondados
dst=cv2.cornerHarris(gray,14,5,0.2)
dst=cv2.dilate(dst,None)

img[dst>0.01*dst.max()]=[0,0,0]

cv2.imshow('cantos',img)
cv2.waitKey()
