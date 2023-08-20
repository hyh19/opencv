# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread('lena.bmp')
rows, cols = img.shape[:2]
mask = np.zeros((rows, cols), dtype=np.uint8)
mask[100:400, 200:400] = 255
mask[100:500, 100:200] = 255
result = cv.bitwise_and(img, img, mask=mask)
cv.imshow('img', img)
cv.imshow('mask', mask)
cv.imshow('result', result)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/L4BoVF
