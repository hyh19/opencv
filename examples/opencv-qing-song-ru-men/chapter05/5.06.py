# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://bit.ly/3ZxNEBX

img = cv.imread('lena.bmp')
ySize, xSize = img.shape[:2]
M = cv.getRotationMatrix2D((xSize / 2, ySize / 2), 45, 0.6)
rotate = cv.warpAffine(img, M, (xSize, ySize))
cv.imshow('original', img)
cv.imshow('rotation', rotate)
cv.waitKey()
cv.destroyAllWindows()
