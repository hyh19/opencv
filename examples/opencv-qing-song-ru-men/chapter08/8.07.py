# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img1 = cv.imread('opening.bmp')
img2 = cv.imread('opening2.bmp')

kernel = np.ones((10, 10), np.uint8)
open_img1 = cv.morphologyEx(img1, cv.MORPH_OPEN, kernel)
open_img2 = cv.morphologyEx(img2, cv.MORPH_OPEN, kernel)

cv.imshow('img1', img1)
cv.imshow('open1', open_img1)
cv.imshow('img2', img2)
cv.imshow('open2', open_img2)

cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://bit.ly/3JJp7TM
