import cv2
import imutils

## Read
img = cv2.imread("C:\\Users\\Martim\\OneDrive\\Scripts Python\\engrenagens\\engrenagem4.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## threshold and find contours
ret, threshed = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)
_, contours, hierarchy = cv2.findContours(threshed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

## Find the max-area-contour
cnt = sorted(contours, key=cv2.contourArea)[-1]

## Approx the contour
arclen = cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, 0.002*arclen, True)
print(len(approx))
## Draw and output the result
for pt in approx:
    cv2.circle(img, (pt[0][0],pt[0][1]), 3, (0,255,0), -1, cv2.LINE_AA)

msg = "Total: {}".format(len(approx)//2)
cv2.putText(img, msg, (20,40),cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 2, cv2.LINE_AA)

## Display
cv2.imshow("res", img);cv2.waitKey()