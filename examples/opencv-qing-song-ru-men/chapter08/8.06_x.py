# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread('dilate.bmp', cv.IMREAD_UNCHANGED)
kernel = np.ones((5, 5), np.uint8)
dilate = cv.dilate(img, kernel, iterations=9)
cv.imshow('img', img)
cv.imshow('dilate', dilate)
cv.waitKey()
cv.destroyAllWindows()
