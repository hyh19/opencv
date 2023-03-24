# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://bit.ly/3z1D0rc

img = cv.imread('kernel.bmp', cv.IMREAD_UNCHANGED)

rect = cv.getStructuringElement(cv.MORPH_RECT, (59, 59))
cross = cv.getStructuringElement(cv.MORPH_CROSS, (59, 59))
ellipse = cv.getStructuringElement(cv.MORPH_ELLIPSE, (59, 59))

dilate1 = cv.dilate(img, rect)
dilate2 = cv.dilate(img, cross)
dilate3 = cv.dilate(img, ellipse)

cv.imshow('img', img)
cv.imshow('dilate1', dilate1)
cv.imshow('dilate2', dilate2)
cv.imshow('dilate3', dilate3)

cv.waitKey()
cv.destroyAllWindows()
