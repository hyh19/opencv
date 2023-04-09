# -*- coding: utf-8 -*-
import cv2 as cv

gray_img = cv.imread('scharr.bmp', cv.IMREAD_GRAYSCALE)

scharr_x_img = cv.Scharr(gray_img, cv.CV_64F, 1, 0)
scharr_x_img = cv.convertScaleAbs(scharr_x_img)

scharr_y_img = cv.Scharr(gray_img, cv.CV_64F, 0, 1)
scharr_y_img = cv.convertScaleAbs(scharr_y_img)

scharr_xy = cv.addWeighted(scharr_x_img, 0.5, scharr_y_img, 0.5, 0)

cv.imshow('gray', gray_img)
cv.imshow('scharr_x', scharr_x_img)
cv.imshow('scharr_y', scharr_y_img)
cv.imshow('scharr_xy', scharr_xy)

cv.waitKey()
cv.destroyAllWindows()
