# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

o1 = cv.imread('tophat.bmp', cv.IMREAD_UNCHANGED)
o2 = cv.imread('lena.bmp', cv.IMREAD_UNCHANGED)
k = np.ones((5, 5), np.uint8)
r1 = cv.morphologyEx(o1, cv.MORPH_TOPHAT, k)
r2 = cv.morphologyEx(o2, cv.MORPH_TOPHAT, k)
cv.imshow('original1', o1)
cv.imshow('original2', o2)
cv.imshow('result1', r1)
cv.imshow('result2', r2)
cv.waitKey()
cv.destroyAllWindows()
