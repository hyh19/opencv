# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('lena.bmp')
rows, cols = img.shape[:2]
width, height = cols, rows
M = cv.getRotationMatrix2D((width / 2, height / 2), 45, 0.6)
res = cv.warpAffine(img, M, (width, height))
cv.imshow('img', img)
cv.imshow('res', res)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/mkRbGr
