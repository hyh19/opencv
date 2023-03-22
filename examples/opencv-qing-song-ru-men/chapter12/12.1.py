# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread('contours.bmp')
cv.imshow("original", o)
gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
image, contours, hierarchy = cv.findContours(binary,
                                              cv.RETR_EXTERNAL,
                                              cv.CHAIN_APPROX_SIMPLE)
o = cv.drawContours(o, contours, -1, (0, 0, 255), 5)
cv.imshow("result", o)
cv.waitKey()
cv.destroyAllWindows()
