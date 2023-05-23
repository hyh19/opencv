# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('kernel.bmp')

kernel_rect = cv.getStructuringElement(cv.MORPH_RECT, (59, 59))
kernel_cross = cv.getStructuringElement(cv.MORPH_CROSS, (59, 59))
kernel_ellipse = cv.getStructuringElement(cv.MORPH_ELLIPSE, (59, 59))

img_rect = cv.dilate(img, kernel_rect)
img_cross = cv.dilate(img, kernel_cross)
img_ellipse = cv.dilate(img, kernel_ellipse)

cv.imshow('img', img)
cv.imshow('rect', img_rect)
cv.imshow('cross', img_cross)
cv.imshow('ellipse', img_ellipse)

cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/xtmpwt