# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread('sobel4.bmp', cv.IMREAD_GRAYSCALE)
scharrx = cv.Sobel(o, cv.CV_64F, 1, 0, -1)
scharry = cv.Sobel(o, cv.CV_64F, 0, 1, -1)
scharrx = cv.convertScaleAbs(scharrx)  # 转回uint8
scharry = cv.convertScaleAbs(scharry)
cv.imshow('original', o)
cv.imshow('x', scharrx)
cv.imshow('y', scharry)
cv.waitKey()
cv.destroyAllWindows()
