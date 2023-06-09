# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('bilTest.bmp')
img_gaussian = r = cv.GaussianBlur(img, (55, 55), 0, 0)
img_bilateral = cv.bilateralFilter(img, 55, 100, 100)
cv.imshow('img', img)
cv.imshow('gaussian', img_gaussian)
cv.imshow('bilateral', img_bilateral)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/TumFFY
