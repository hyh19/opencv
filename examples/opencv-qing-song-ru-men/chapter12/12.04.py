# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

o = cv.imread('moments.bmp')
cv.imshow("original", o)
gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
image, contours, hierarchy = cv.findContours(binary,
                                              cv.RETR_LIST,
                                              cv.CHAIN_APPROX_SIMPLE)
n = len(contours)
contoursImg = []
for i in range(n):
    temp = np.zeros(image.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i] = cv.drawContours(contoursImg[i], contours, i, 255, 3)
    cv.imshow("contours[" + str(i) + "]", contoursImg[i])
print("观察各个轮廓的矩（moments）:")
for i in range(n):
    print("轮廓" + str(i) + "的矩:\n", cv.moments(contours[i]))
print("观察各个轮廓的面积:")
for i in range(n):
    print("轮廓" + str(i) + "的面积:%d" % cv.moments(contours[i])['m00'])
cv.waitKey()
cv.destroyAllWindows()
