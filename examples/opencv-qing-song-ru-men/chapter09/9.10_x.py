# -*- coding: utf-8 -*-
import cv2 as cv

img_gray = cv.imread('scharr.bmp', cv.IMREAD_GRAYSCALE)

scharr_x = cv.Scharr(img_gray, cv.CV_64F, 1, 0)
scharr_x = cv.convertScaleAbs(scharr_x)

scharr_y = cv.Scharr(img_gray, cv.CV_64F, 0, 1)
scharr_y = cv.convertScaleAbs(scharr_y)

scharr_xy = cv.addWeighted(scharr_x, 0.5, scharr_y, 0.5, 0)

cv.imshow('img_gray', img_gray)
cv.imshow('scharr_x', scharr_x)
cv.imshow('scharr_y', scharr_y)
cv.imshow('scharr_xy', scharr_xy)

cv.waitKey()
cv.destroyAllWindows()
