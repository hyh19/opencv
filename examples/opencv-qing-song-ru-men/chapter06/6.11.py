# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('computer.jpg')
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thresh_img = cv.threshold(gray_img, 127, 255, cv.THRESH_BINARY)
mean_img = cv.adaptiveThreshold(gray_img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, 5)
gaussian_img = cv.adaptiveThreshold(gray_img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 3, 5)

cv.imshow('img', img)
cv.imshow('gray', gray_img)
cv.imshow('thresh', thresh_img)
cv.imshow('mean', mean_img)
cv.imshow('gaussian', gaussian_img)

cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/bgBlss
