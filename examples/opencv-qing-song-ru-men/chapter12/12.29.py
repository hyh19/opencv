# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread('cc.bmp')
cv.imshow("original", o)
gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
image, contours, hierarchy = cv.findContours(binary,
                                              cv.RETR_LIST,
                                              cv.CHAIN_APPROX_SIMPLE)
x, y, w, h = cv.boundingRect(contours[0])
cv.drawContours(o, contours[0], -1, (0, 0, 255), 3)
cv.rectangle(o, (x, y), (x + w, y + h), (255, 0, 0), 3)
rectArea = w * h
cntArea = cv.contourArea(contours[0])
extend = float(cntArea) / rectArea
print(extend)
cv.imshow("result", o)
cv.waitKey()
cv.destroyAllWindows()
