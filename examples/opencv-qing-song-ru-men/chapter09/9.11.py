# -*- coding: utf-8 -*-
import cv2 as cv

gray_img = cv.imread('scharr.bmp', cv.IMREAD_GRAYSCALE)
scharr_xy_img = cv.Scharr(gray_img, cv.CV_64F, 1, 1)
cv.imshow('gray', gray_img)
cv.imshow('scharr_xy', scharr_xy_img)
cv.waitKey()
cv.destroyAllWindows()
