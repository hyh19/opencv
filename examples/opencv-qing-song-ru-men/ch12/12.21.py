# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('hand.bmp')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, img_binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)
_, contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

red = (0, 0, 255)
green = (0, 255, 0)

cv.drawContours(img, contours, 0, red, 2)
hull = cv.convexHull(contours[0])
cv.polylines(img, [hull], True, green, 2)

cv.imshow("result", img)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/sgi4in
