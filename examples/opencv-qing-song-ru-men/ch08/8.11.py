# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img1 = cv.imread('blackhat.bmp')
img2 = cv.imread('lena.bmp')

kernel = np.ones(shape=(5, 5), dtype=np.uint8)
img1_blackhat = cv.morphologyEx(img1, cv.MORPH_BLACKHAT, kernel)
img2_blackhat = cv.morphologyEx(img2, cv.MORPH_BLACKHAT, kernel)

cv.imshow('img1', img1)
cv.imshow('blackhat1', img1_blackhat)
cv.imshow('img2', img2)
cv.imshow('blackhat2', img2_blackhat)

cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://bit.ly/3lCnyie
