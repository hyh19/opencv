# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('lena.bmp')
flip_row = cv.flip(img, 0)
flip_col = cv.flip(img, 1)
flip_row_col = cv.flip(img, -1)
cv.imshow('img', img)
cv.imshow('flip_row', flip_row)
cv.imshow('flip_col', flip_col)
cv.imshow('flip_row_col', flip_row_col)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/cwi944
