# -*- coding: utf-8 -*-
import cv2 as cv

img_gray = cv.imread('scharr.bmp', cv.IMREAD_GRAYSCALE)

img_scharr_x = cv.Scharr(img_gray, cv.CV_64F, 1, 0)
img_scharr_x = cv.convertScaleAbs(img_scharr_x)

img_scharr_y = cv.Scharr(img_gray, cv.CV_64F, 0, 1)
img_scharr_y = cv.convertScaleAbs(img_scharr_y)

scharr_xy = cv.addWeighted(img_scharr_x, 0.5, img_scharr_y, 0.5, 0)

cv.imshow('gray', img_gray)
cv.imshow('scharr_x', img_scharr_x)
cv.imshow('scharr_y', img_scharr_y)
cv.imshow('scharr_xy', scharr_xy)

cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/nMfEWA
