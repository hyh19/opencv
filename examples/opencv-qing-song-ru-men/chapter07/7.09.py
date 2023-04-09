# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('bilTest.bmp')
gaussian_img = r = cv.GaussianBlur(img, (55, 55), 0, 0)
bilateral_img = cv.bilateralFilter(img, 55, 100, 100)
cv.imshow('img', img)
cv.imshow('gaussian', gaussian_img)
cv.imshow('bilateral', bilateral_img)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/TumFFY
