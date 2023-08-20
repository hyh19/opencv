# -*- coding: utf-8 -*-
import cv2 as cv

img_gray = cv.imread('sobel4.bmp', cv.IMREAD_GRAYSCALE)
img_sobel_x = cv.Sobel(img_gray, cv.CV_64F, 1, 0)
img_sobel_x = cv.convertScaleAbs(img_sobel_x)
cv.imshow('gray', img_gray)
cv.imshow('sobel_x', img_sobel_x)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/wSArrU
