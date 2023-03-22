# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

opencv = cv.imread("opencv.jpg")
hsv = cv.cvtColor(opencv, cv.COLOR_BGR2HSV)
cv.imshow('opencv', opencv)

# =============指定蓝色值的范围=============
minBlue = np.array([110, 50, 50])
maxBlue = np.array([130, 255, 255])
# 确定蓝色区域
mask = cv.inRange(hsv, minBlue, maxBlue)
# 通过掩码控制的按位与，锁定蓝色区域
blue = cv.bitwise_and(opencv, opencv, mask=mask)
cv.imshow('blue', blue)

# =============指定绿色值的范围=============
minGreen = np.array([50, 50, 50])
maxGreen = np.array([70, 255, 255])
# 确定绿色区域
mask = cv.inRange(hsv, minGreen, maxGreen)
# 通过掩码控制的按位与，锁定绿色区域
green = cv.bitwise_and(opencv, opencv, mask=mask)
cv.imshow('green', green)

# =============指定红色值的范围=============
minRed = np.array([0, 50, 50])
maxRed = np.array([30, 255, 255])
# 确定红色区域
mask = cv.inRange(hsv, minRed, maxRed)
# 通过掩码控制的按位与，锁定红色区域
red = cv.bitwise_and(opencv, opencv, mask=mask)
cv.imshow('red', red)

cv.waitKey()
cv.destroyAllWindows()
