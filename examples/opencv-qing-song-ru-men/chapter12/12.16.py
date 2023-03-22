# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread('cc.bmp')
cv.imshow("original", o)

gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
image, contours, hierarchy = cv.findContours(binary,
                                              cv.RETR_LIST,
                                              cv.CHAIN_APPROX_SIMPLE)

ellipse = cv.fitEllipse(contours[0])
print("ellipse=", ellipse)

cv.ellipse(o, ellipse, (0, 255, 0), 3)
cv.imshow("result", o)

cv.waitKey()
cv.destroyAllWindows()
