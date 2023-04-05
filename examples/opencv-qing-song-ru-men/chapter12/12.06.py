# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

o = cv.imread('contours.bmp')
cv.imshow("original", o)
gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
image, contours, hierarchy = cv.findContours(binary,
                                              cv.RETR_LIST,
                                              cv.CHAIN_APPROX_SIMPLE)
n = len(contours)
contoursImg = []
for i in range(n):
    temp = np.zeros(o.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i] = cv.drawContours(contoursImg[i],
                                      contours, i, (255, 255, 255), 3)
    if cv.contourArea(contours[i]) > 15000:
        cv.imshow("contours[" + str(i) + "]", contoursImg[i])
cv.waitKey()
cv.destroyAllWindows()
