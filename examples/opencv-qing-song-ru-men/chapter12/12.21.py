# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://is.gd/sgi4in

img = cv.imread('hand.bmp')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
_, contours, hierarchy = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contours, 0, (0, 0, 255), 2)
hull = cv.convexHull(contours[0])
cv.polylines(img, [hull], True, (0, 255, 0), 2)
cv.imshow("result", img)
cv.waitKey()
cv.destroyAllWindows()
