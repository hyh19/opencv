# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread('lenaNoise.png')
r = cv.bilateralFilter(o, 25, 100, 100)
cv.imshow('original', o)
cv.imshow('result', r)
cv.waitKey()
cv.destroyAllWindows()
