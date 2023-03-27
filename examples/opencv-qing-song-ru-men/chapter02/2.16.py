# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://is.gd/Bm8d2O

lena = cv.imread('lenacolor.png')
cv.imshow('lena', lena)

blue = lena[:, :, 0]
green = lena[:, :, 1]
red = lena[:, :, 2]
cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)

lena[:, :, 0] = 0
cv.imshow('lena_blue0', lena)

lena[:, :, 1] = 0
cv.imshow('lena_blue0_green0', lena)

cv.waitKey()
cv.destroyAllWindows()
