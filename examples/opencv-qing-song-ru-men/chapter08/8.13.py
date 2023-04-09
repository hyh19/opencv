# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('kernel.bmp')

rect_kernel = cv.getStructuringElement(cv.MORPH_RECT, (59, 59))
cross_kernel = cv.getStructuringElement(cv.MORPH_CROSS, (59, 59))
ellipse_kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (59, 59))

rect_dilate_img = cv.dilate(img, rect_kernel)
cross_dilate_img = cv.dilate(img, cross_kernel)
ellipse_dilate_img = cv.dilate(img, ellipse_kernel)

cv.imshow('img', img)
cv.imshow('rect_dilate', rect_dilate_img)
cv.imshow('cross_dilate', cross_dilate_img)
cv.imshow('ellipse_dilate', ellipse_dilate_img)

cv.waitKey()
cv.destroyAllWindows()

# 修改标题
# 运行结果 https://bit.ly/3z1D0rc
