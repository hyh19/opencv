# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://is.gd/V9Oxnw

bgr = cv.imread('lena.bmp')
mask = np.zeros(bgr.shape, dtype=np.uint8)
mask[100:400, 200:400] = 255
mask[100:500, 100:200] = 255
result = cv.bitwise_and(bgr, mask)
cv.imshow('bgr', bgr)
cv.imshow('mask', mask)
cv.imshow('result', result)
cv.waitKey()
cv.destroyAllWindows()
