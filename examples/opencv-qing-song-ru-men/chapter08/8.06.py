# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread('dilation.bmp', cv.IMREAD_UNCHANGED)
kernel = np.ones((5, 5), np.uint8)
img_dilate = cv.dilate(img, kernel, iterations=9)
cv.imshow('img', img)
cv.imshow('dilate', img_dilate)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://bit.ly/3lJjxJ1
