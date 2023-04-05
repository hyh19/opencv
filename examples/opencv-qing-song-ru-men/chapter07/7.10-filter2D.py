# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://is.gd/T02aKP

img = cv.imread('lena.bmp')
kernel = np.ones((9, 9), np.float32) / 81
res = cv.filter2D(img, -1, kernel)
cv.imshow('img', img)
cv.imshow('res', res)
cv.waitKey()
cv.destroyAllWindows()
