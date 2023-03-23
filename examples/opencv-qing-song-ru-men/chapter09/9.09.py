# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread('scharr.bmp', cv.IMREAD_GRAYSCALE)
scharry = cv.Scharr(o, cv.CV_64F, 0, 1)
scharry = cv.convertScaleAbs(scharry)
cv.imshow('original', o)
cv.imshow('y', scharry)
cv.waitKey()
cv.destroyAllWindows()
