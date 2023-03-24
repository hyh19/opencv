# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

o = cv.imread('erode.bmp', cv.IMREAD_UNCHANGED)
kernel = np.ones((5, 5), np.uint8)
erosion = cv.erode(o, kernel)
cv.imshow('original', o)
cv.imshow('erosion', erosion)
cv.waitKey()
cv.destroyAllWindows()
