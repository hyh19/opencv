# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img1 = cv.imread('tophat.bmp')
img2 = cv.imread('lena.bmp')

kernel = np.ones(shape=(5, 5), dtype=np.uint8)
img1_tophat = cv.morphologyEx(img1, cv.MORPH_TOPHAT, kernel)
img2_tophat = cv.morphologyEx(img2, cv.MORPH_TOPHAT, kernel)

cv.imshow('img1', img1)
cv.imshow('tophat1', img1_tophat)
cv.imshow('img2', img2)
cv.imshow('tophat2', img2_tophat)

cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://bit.ly/3LJwEVa
