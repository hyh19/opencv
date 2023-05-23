# -*- coding: utf-8 -*-
import cv2 as cv

img_gray = cv.imread('sobel4.bmp', cv.IMREAD_GRAYSCALE)
img_scharr_x = cv.Sobel(img_gray, cv.CV_64F, 1, 0, -1)
img_scharr_x = cv.convertScaleAbs(img_scharr_x)

img_scharr_y = cv.Sobel(img_gray, cv.CV_64F, 0, 1, -1)
img_scharr_y = cv.convertScaleAbs(img_scharr_y)

cv.imshow('gray', img_gray)
cv.imshow('scharr_x', img_scharr_x)
cv.imshow('scharr_y', img_scharr_y)

cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/l5ZtUn
