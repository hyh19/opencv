# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img1 = cv.imread('blackhat.bmp')
img2 = cv.imread('lena.bmp')

kernel = np.ones((5, 5), np.uint8)
blackhat_img1 = cv.morphologyEx(img1, cv.MORPH_BLACKHAT, kernel)
blackhat_img2 = cv.morphologyEx(img2, cv.MORPH_BLACKHAT, kernel)

cv.imshow('img1', img1)
cv.imshow('blackhat1', blackhat_img1)
cv.imshow('img2', img2)
cv.imshow('blackhat2', blackhat_img2)

cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://bit.ly/3lCnyie
