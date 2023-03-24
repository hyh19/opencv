# -*- coding: utf-8 -*-
import cv2 as cv

img_gray = cv.imread('lena.bmp', cv.IMREAD_GRAYSCALE)

sobel_x = cv.Sobel(img_gray, cv.CV_64F, 1, 0, ksize=3)
sobel_x = cv.convertScaleAbs(sobel_x)
sobel_y = cv.Sobel(img_gray, cv.CV_64F, 0, 1, ksize=3)
sobel_y = cv.convertScaleAbs(sobel_y)
sobel_xy = cv.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

scharr_x = cv.Scharr(img_gray, cv.CV_64F, 1, 0)
scharr_x = cv.convertScaleAbs(scharr_x)
scharr_y = cv.Scharr(img_gray, cv.CV_64F, 0, 1)
scharr_y = cv.convertScaleAbs(scharr_y)
scharr_xy = cv.addWeighted(scharr_x, 0.5, scharr_y, 0.5, 0)

cv.imshow('img_gray', img_gray)
cv.imshow('sobel_xy', sobel_xy)
cv.imshow('scharr_xy', scharr_xy)

cv.waitKey()
cv.destroyAllWindows()
