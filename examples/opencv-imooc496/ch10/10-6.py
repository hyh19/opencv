import cv2 as cv
import numpy as np

img = cv.imread('../images/hello.jpeg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, img_bin = cv.threshold(img_gray, thresh=150, maxval=255, type=cv.THRESH_BINARY)

# 查找轮廓
contours, hierarchy = cv.findContours(img_bin, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_SIMPLE)

# 绘制轮廓
cv.drawContours(img, contours, contourIdx=-1, color=(0, 0, 255), thickness=1)

r = cv.minAreaRect(contours[1])
box = cv.boxPoints(r)
box = np.intp(box)
cv.drawContours(img, contours=[box], contourIdx=0, color=(0, 255, 0), thickness=2)

x, y, w, h = cv.boundingRect(contours[1])
cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv.imshow('img', img)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()

# minAreaRect: https://t.ly/MhzA
# boxPoints: https://t.ly/T0ij
# boundingRect: https://t.ly/ozJs
