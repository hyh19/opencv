# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread('erode.bmp', cv.IMREAD_UNCHANGED)
kernel = np.ones((5, 5), np.uint8)
erode = cv.erode(img, kernel)
cv.imshow('img', img)
cv.imshow('erode', erode)
cv.waitKey()
cv.destroyAllWindows()
