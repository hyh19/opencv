# -*- coding: utf-8 -*-
import cv2 as cv

gray_img = cv.imread('scharr.bmp', cv.IMREAD_GRAYSCALE)
scharr_x_img = cv.Scharr(gray_img, cv.CV_64F, 1, 0)
scharr_x_img = cv.convertScaleAbs(scharr_x_img)
cv.imshow('gray', gray_img)
cv.imshow('scharr_x', scharr_x_img)
cv.waitKey()
cv.destroyAllWindows()
