import numpy as np
import cv2

img = cv2.imread('C:\\Users\\Martim\\OneDrive\\Scripts Python\\engrenagens\\engrenagem1.jpg')
#img2 = cv2.imread('C:\\Users\\Link\\Desktop\\gear.png')
img2 = cv2.imread('C:\\Users\\Martim\\OneDrive\\Scripts Python\\engrenagens\\engrenagem1.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

kernel = np.ones((3, 3), np.uint8)

img_dilate = cv2.dilate(thresh, kernel, iterations=1)

im2, contours, hierarchy = cv2.findContours(img_dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cv2.drawContours(img, contours, -1, (0, 255, 0), -1)

edges = cv2.Canny(cnts, 350, 350)

cnt = contours[0]

hull = cv2.convexHull(cnt, returnPoints=False)
defects = cv2.convexityDefects(cnt, hull)

for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(edges, start, end, [0, 255, 255], 1)
    circles = cv2.circle(img2, end, 5, [0, 255, 0], -1)


# print(len(defects)) - number of points

cv2.imshow('thresh', thresh)
cv2.waitKey(0)
cv2.imshow('dilate', img_dilate)
cv2.waitKey(0)
cv2.imshow('edges', edges)
cv2.waitKey(0)
cv2.imshow('cnts', cnts)
cv2.waitKey(0)
cv2.imshow('points', circles)
cv2.waitKey(0)