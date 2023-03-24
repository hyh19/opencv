# -*- coding: utf-8 -*-
import cv2 as cv

img_gray = cv.imread('sobel4.bmp', cv.IMREAD_GRAYSCALE)
scharr_x = cv.Sobel(img_gray, cv.CV_64F, 1, 0, -1)
scharr_x = cv.convertScaleAbs(scharr_x)

scharr_y = cv.Sobel(img_gray, cv.CV_64F, 0, 1, -1)
scharr_y = cv.convertScaleAbs(scharr_y)

cv.imshow('img_gray', img_gray)
cv.imshow('scharr_x', scharr_x)
cv.imshow('scharr_y', scharr_y)

cv.waitKey()
cv.destroyAllWindows()
