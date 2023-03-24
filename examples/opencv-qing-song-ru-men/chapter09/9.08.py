# -*- coding: utf-8 -*-
import cv2 as cv

img_gray = cv.imread('scharr.bmp', cv.IMREAD_GRAYSCALE)
scharr_x = cv.Scharr(img_gray, cv.CV_64F, 1, 0)
scharr_x = cv.convertScaleAbs(scharr_x)
cv.imshow('img_gray', img_gray)
cv.imshow('scharr_x', scharr_x)
cv.waitKey()
cv.destroyAllWindows()
