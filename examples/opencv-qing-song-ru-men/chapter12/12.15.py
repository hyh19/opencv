# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread('cc.bmp')
cv.imshow("original", o)

gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
image, contours, hierarchy = cv.findContours(binary,
                                              cv.RETR_LIST,
                                              cv.CHAIN_APPROX_SIMPLE)

(x, y), radius = cv.minEnclosingCircle(contours[0])
center = (int(x), int(y))
radius = int(radius)
cv.circle(o, center, radius, (0, 0, 255), 2)
cv.imshow("result", o)

cv.waitKey()
cv.destroyAllWindows()
