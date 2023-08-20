# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread('gradient.bmp')
kernel = np.ones((5, 5), np.uint8)
img_gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
cv.imshow('img', img)
cv.imshow('gradient', img_gradient)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://bit.ly/3z3SCKY
