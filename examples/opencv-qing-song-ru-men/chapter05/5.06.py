# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('lena.bmp')
ySize, xSize = img.shape[:2]
M = cv.getRotationMatrix2D((xSize / 2, ySize / 2), 45, 0.6)
res = cv.warpAffine(img, M, (xSize, ySize))
cv.imshow('img', img)
cv.imshow('res', res)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/mkRbGr
