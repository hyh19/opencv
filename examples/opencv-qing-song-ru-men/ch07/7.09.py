# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('bilTest.bmp')
img_gaussian = cv.GaussianBlur(img, ksize=(55, 55), sigmaX=0, sigmaY=0)
img_bilateral = cv.bilateralFilter(img, d=55, sigmaColor=100, sigmaSpace=100)
cv.imshow('img', img)
cv.imshow('gaussian', img_gaussian)
cv.imshow('bilateral', img_bilateral)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/TumFFY
