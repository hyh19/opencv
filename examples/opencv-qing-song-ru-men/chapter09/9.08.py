# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread('scharr.bmp', cv.IMREAD_GRAYSCALE)
scharrx = cv.Scharr(o, cv.CV_64F, 1, 0)
scharrx = cv.convertScaleAbs(scharrx)  # 转回uint8
cv.imshow('original', o)
cv.imshow('x', scharrx)
cv.waitKey()
cv.destroyAllWindows()
