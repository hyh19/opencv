# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread('lena.bmp')
ySize, xSize = img.shape[:2]
xMove, yMove = 100, 200
M = np.float32([[1, 0, xMove], [0, 1, yMove]])
res = cv.warpAffine(img, M, (xSize, ySize))
cv.imshow('img', img)
cv.imshow('res', res)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/h6JwgQ
