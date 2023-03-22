# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread('hand.bmp')
cv.imshow("original", o)
gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
image, contours, hierarchy = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(o, contours[0], -1, (0, 0, 255), 3)
cntArea = cv.contourArea(contours[0])
hull = cv.convexHull(contours[0])
hullArea = cv.contourArea(hull)
cv.polylines(o, [hull], True, (0, 255, 0), 2)
solidity = float(cntArea) / hullArea
print(solidity)
cv.imshow("result", o)
cv.waitKey()
cv.destroyAllWindows()
