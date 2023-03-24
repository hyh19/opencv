# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img1 = cv.imread('closing.bmp')
img2 = cv.imread('closing2.bmp')

kernel = np.ones((10, 10), np.uint8)
close1 = cv.morphologyEx(img1, cv.MORPH_CLOSE, kernel, iterations=3)
close2 = cv.morphologyEx(img2, cv.MORPH_CLOSE, kernel, iterations=3)

cv.imshow('img1', img1)
cv.imshow('close1', close1)
cv.imshow('img2', img2)
cv.imshow('close2', close2)

cv.waitKey()
cv.destroyAllWindows()
