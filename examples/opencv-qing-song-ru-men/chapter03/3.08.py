# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

gray = cv.imread('lena.bmp', cv.IMREAD_GRAYSCALE)
mask = np.zeros(gray.shape, dtype=np.uint8)
mask[100:400, 200:400] = 255
mask[100:500, 100:200] = 255
result = cv.bitwise_and(gray, mask)
cv.imshow('gray', gray)
cv.imshow('mask', mask)
cv.imshow('result', result)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/R00NLQ
