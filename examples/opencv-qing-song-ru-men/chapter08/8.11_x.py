# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://bit.ly/3lCnyie

img1 = cv.imread('blackhat.bmp', cv.IMREAD_UNCHANGED)
img2 = cv.imread('lena.bmp', cv.IMREAD_UNCHANGED)

kernel = np.ones((5, 5), np.uint8)
blackhat1 = cv.morphologyEx(img1, cv.MORPH_BLACKHAT, kernel)
blackhat2 = cv.morphologyEx(img2, cv.MORPH_BLACKHAT, kernel)

cv.imshow('img1', img1)
cv.imshow('img2', img2)
cv.imshow('blackhat1', blackhat1)
cv.imshow('blackhat2', blackhat2)

cv.waitKey()
cv.destroyAllWindows()
