# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img1 = cv.imread('opening.bmp')
img2 = cv.imread('opening2.bmp')

kernel = np.ones((10, 10), np.uint8)
open1 = cv.morphologyEx(img1, cv.MORPH_OPEN, kernel)
open2 = cv.morphologyEx(img2, cv.MORPH_OPEN, kernel)

cv.imshow('img1', img1)
cv.imshow('open1', open1)
cv.imshow('img2', img2)
cv.imshow('open2', open2)

cv.waitKey()
cv.destroyAllWindows()
