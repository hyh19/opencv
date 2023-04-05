# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('cc.bmp')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
_, contours, hierarchy = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(img, contours, 0, (0, 0, 255), 2)
ellipse = cv.fitEllipse(contours[0])
print(f'ellipse = \n{ellipse}')
cv.ellipse(img, ellipse, (255, 0, 0), 3)
cv.imshow('result', img)
cv.waitKey()
cv.destroyAllWindows()
