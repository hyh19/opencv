# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img1 = cv.imread('closing.bmp')
img2 = cv.imread('closing2.bmp')

kernel = np.ones(shape=(10, 10), dtype=np.uint8)
img1_close = cv.morphologyEx(img1, cv.MORPH_CLOSE, kernel, iterations=3)
img2_close = cv.morphologyEx(img2, cv.MORPH_CLOSE, kernel, iterations=3)

cv.imshow('img1', img1)
cv.imshow('close1', img1_close)
cv.imshow('img2', img2)
cv.imshow('close2', img2_close)

cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://bit.ly/40l4rsb
