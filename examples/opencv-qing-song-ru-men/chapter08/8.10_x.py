# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://bit.ly/3LJwEVa

img1 = cv.imread('tophat.bmp', cv.IMREAD_UNCHANGED)
img2 = cv.imread('lena.bmp', cv.IMREAD_UNCHANGED)

kernel = np.ones((5, 5), np.uint8)
tophat1 = cv.morphologyEx(img1, cv.MORPH_TOPHAT, kernel)
tophat2 = cv.morphologyEx(img2, cv.MORPH_TOPHAT, kernel)

cv.imshow('img1', img1)
cv.imshow('img2', img2)
cv.imshow('tophat1', tophat1)
cv.imshow('tophat2', tophat2)

cv.waitKey()
cv.destroyAllWindows()
