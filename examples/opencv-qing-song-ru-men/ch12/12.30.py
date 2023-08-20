# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('hand.bmp')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, img_binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)

red = (0, 0, 255)
green = (0, 255, 0)

_, contours, _ = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contours, 0, red, 2)
cnt_area = cv.contourArea(contours[0])

hull = cv.convexHull(contours[0])
hull_area = cv.contourArea(hull)
cv.polylines(img, [hull], True, green, 2)
print(f'Solidity = {cnt_area / hull_area}')

cv.imshow("result", img)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/t0Dk9n
