# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

o = cv.imread('gradient.bmp', cv.IMREAD_UNCHANGED)
k = np.ones((5, 5), np.uint8)
r = cv.morphologyEx(o, cv.MORPH_GRADIENT, k)
cv.imshow('original', o)
cv.imshow('result', r)
cv.waitKey()
cv.destroyAllWindows()
