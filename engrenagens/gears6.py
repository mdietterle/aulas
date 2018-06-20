import cv2

img = cv2.imread('C:\\Users\\Martim\\OneDrive\\Scripts Python\\engrenagens\\engre2.png',cv2.IMREAD_COLOR)

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
bilateral = cv2.bilateralFilter(gray, 9, 75, 75)
canny = cv2.Canny(bilateral, 50, 150)

corners    = cv2.goodFeaturesToTrack(canny,200,0.2,25)

for i in range(len(corners)):
    cv2.circle(img, (corners[i][0][0], corners[i][0][1]), 5, 255, -1)

cv2.imshow('dilated', img)
cv2.waitKey(0)