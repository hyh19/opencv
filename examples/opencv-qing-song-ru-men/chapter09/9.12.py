# -*- coding: utf-8 -*-
import cv2 as cv

gray_img = cv.imread('sobel4.bmp', cv.IMREAD_GRAYSCALE)
scharr_x_img = cv.Sobel(gray_img, cv.CV_64F, 1, 0, -1)
scharr_x_img = cv.convertScaleAbs(scharr_x_img)

scharr_y_img = cv.Sobel(gray_img, cv.CV_64F, 0, 1, -1)
scharr_y_img = cv.convertScaleAbs(scharr_y_img)

cv.imshow('gray', gray_img)
cv.imshow('scharr_x', scharr_x_img)
cv.imshow('scharr_y', scharr_y_img)

cv.waitKey()
cv.destroyAllWindows()
