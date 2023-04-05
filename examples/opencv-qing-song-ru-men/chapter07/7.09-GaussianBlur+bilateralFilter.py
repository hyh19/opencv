# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('bilTest.bmp')
gaussian = r = cv.GaussianBlur(img, (55, 55), 0, 0)
bilateral = cv.bilateralFilter(img, 55, 100, 100)
cv.imshow('img', img)
cv.imshow('gaussian', gaussian)
cv.imshow('bilateral', bilateral)
cv.waitKey()
cv.destroyAllWindows()
