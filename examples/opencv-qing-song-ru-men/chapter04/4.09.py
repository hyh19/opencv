# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://is.gd/T9vQIX

bgr = cv.imread("opencv.jpg")
hsv = cv.cvtColor(bgr, cv.COLOR_BGR2HSV)
cv.imshow('bgr', bgr)

min_blue = np.array([110, 50, 50])
max_blue = np.array([130, 255, 255])
mask = cv.inRange(hsv, min_blue, max_blue)
blue = cv.bitwise_and(bgr, bgr, mask=mask)
cv.imshow('blue', blue)

min_green = np.array([50, 50, 50])
max_green = np.array([70, 255, 255])
mask = cv.inRange(hsv, min_green, max_green)
green = cv.bitwise_and(bgr, bgr, mask=mask)
cv.imshow('green', green)

min_red = np.array([0, 50, 50])
max_red = np.array([30, 255, 255])
mask = cv.inRange(hsv, min_red, max_red)
red = cv.bitwise_and(bgr, bgr, mask=mask)
cv.imshow('red', red)

cv.waitKey()
cv.destroyAllWindows()
