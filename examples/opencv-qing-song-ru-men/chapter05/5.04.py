# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('lena.bmp')
flip_x = cv.flip(img, 0)
flip_y = cv.flip(img, 1)
flip_xy = cv.flip(img, -1)
cv.imshow('img', img)
cv.imshow('flip_x', flip_x)
cv.imshow('flip_y', flip_y)
cv.imshow('flip_xy', flip_xy)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/g2usqj
