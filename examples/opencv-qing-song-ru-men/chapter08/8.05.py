# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread('dilation.bmp')
kernel = np.ones((9, 9), np.uint8)
img_dilate = cv.dilate(img, kernel)
cv.imshow('img', img)
cv.imshow('dilate', img_dilate)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/ZGqRIT
