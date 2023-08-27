# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img1 = cv.imread('opening.bmp')
img2 = cv.imread('opening2.bmp')

kernel = np.ones(shape=(10, 10), dtype=np.uint8)
img1_open = cv.morphologyEx(img1, cv.MORPH_OPEN, kernel)
img2_open = cv.morphologyEx(img2, cv.MORPH_OPEN, kernel)

cv.imshow('img1', img1)
cv.imshow('open1', img1_open)
cv.imshow('img2', img2)
cv.imshow('open2', img2_open)

cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://bit.ly/3JJp7TM
