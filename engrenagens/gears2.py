import numpy as np
import cv2

img = cv2.imread('C:\\Users\\Martim\\OneDrive\\Scripts Python\\engrenagens\\engrenagem2.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

kernel = np.ones((3, 3), np.uint8)

img_erosion = cv2.erode(thresh, kernel, iterations=1)

edges = cv2.Canny(img_erosion, 50, 150)

img_dilate = cv2.dilate(edges, kernel, iterations=1)

cv2.imshow('i', thresh)
cv2.waitKey(0)
cv2.imshow('i', img_erosion)
cv2.waitKey(0)
cv2.imshow('i', edges)
cv2.waitKey(0)
cv2.imshow('i', img_dilate)
cv2.waitKey(0)