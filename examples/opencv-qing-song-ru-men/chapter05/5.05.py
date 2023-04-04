# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://bit.ly/3T3oh8z

img = cv.imread('lena.bmp')
ySize, xSize = img.shape[:2]
xMove = 100
yMove = 200
M = np.float32([[1, 0, xMove], [0, 1, yMove]])
move = cv.warpAffine(img, M, (xSize, ySize))
cv.imshow('original', img)
cv.imshow('move', move)
cv.waitKey()
cv.destroyAllWindows()
