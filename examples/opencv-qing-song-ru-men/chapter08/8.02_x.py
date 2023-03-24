# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread('erode.bmp', cv.IMREAD_UNCHANGED)
kernel = np.ones((5, 5), np.uint8)
erosion = cv.erode(img, kernel)
cv.imshow('img', img)
cv.imshow('erosion', erosion)
cv.waitKey()
cv.destroyAllWindows()
