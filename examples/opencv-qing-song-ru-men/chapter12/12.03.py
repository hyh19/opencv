# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://bit.ly/40iYegB

o = cv.imread('loc3.jpg')
cv.imshow("original", o)
gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
cv.imshow("binary", binary)
image, contours, hierarchy = cv.findContours(binary,
                                              cv.RETR_LIST,
                                              cv.CHAIN_APPROX_SIMPLE)
mask = np.zeros(o.shape, np.uint8)
mask = cv.drawContours(mask, contours, -1, (255, 255, 255), -1)
cv.imshow("mask", mask)
loc = cv.bitwise_and(o, mask)
cv.imshow("location", loc)
cv.waitKey()
cv.destroyAllWindows()
