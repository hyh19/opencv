# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://bit.ly/3J0btLr

img = cv.imread('lena.bmp')
x = cv.flip(img, 0)
y = cv.flip(img, 1)
xy = cv.flip(img, -1)
cv.imshow('img', img)
cv.imshow('x', x)
cv.imshow('y', y)
cv.imshow('xy', xy)
cv.waitKey()
cv.destroyAllWindows()
