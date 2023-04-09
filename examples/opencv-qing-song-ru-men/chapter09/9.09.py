# -*- coding: utf-8 -*-
import cv2 as cv

gray_img = cv.imread('scharr.bmp', cv.IMREAD_GRAYSCALE)
scharr_y_img = cv.Scharr(gray_img, cv.CV_64F, 0, 1)
scharr_y_img = cv.convertScaleAbs(scharr_y_img)
cv.imshow('gray', gray_img)
cv.imshow('scharr_y', scharr_y_img)
cv.waitKey()
cv.destroyAllWindows()
