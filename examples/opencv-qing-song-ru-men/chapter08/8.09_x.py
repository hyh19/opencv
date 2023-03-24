# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread('gradient.bmp', cv.IMREAD_UNCHANGED)
kernel = np.ones((5, 5), np.uint8)
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
cv.imshow('img', img)
cv.imshow('gradient', gradient)
cv.waitKey()
cv.destroyAllWindows()
