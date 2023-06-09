# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('computer.jpg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, img_thresh = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)
img_mean = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, 5)
img_gaussian = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 3, 5)

cv.imshow('img', img)
cv.imshow('gray', img_gray)
cv.imshow('thresh', img_thresh)
cv.imshow('mean', img_mean)
cv.imshow('gaussian', img_gaussian)

cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/bgBlss
