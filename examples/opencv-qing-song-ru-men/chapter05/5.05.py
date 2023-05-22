# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread('lena.bmp')
move_x, move_y = 100, 200
M = np.float32([[1, 0, move_x], [0, 1, move_y]])
rows, cols = img.shape[:2]
width, height = cols, rows
res = cv.warpAffine(img, M, (width, height))
cv.imshow('img', img)
cv.imshow('res', res)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/h6JwgQ
