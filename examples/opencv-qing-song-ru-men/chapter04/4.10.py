# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://bit.ly/3kUm2aW

img = cv.imread("lesson2.jpg")
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
h, s, v = cv.split(hsv)
minHue = 5
maxHue = 170
hueMask = cv.inRange(h, minHue, maxHue)
minSat = 25
maxSat = 166
satMask = cv.inRange(s, minSat, maxSat)
mask = hueMask & satMask
roi = cv.bitwise_and(img, img, mask=mask)
cv.imshow("img", img)
cv.imshow("ROI", roi)
cv.waitKey()
cv.destroyAllWindows()
