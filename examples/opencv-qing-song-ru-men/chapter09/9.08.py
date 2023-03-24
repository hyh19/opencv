# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('scharr.bmp', cv.IMREAD_GRAYSCALE)
scharr_x = cv.Scharr(img, cv.CV_64F, 1, 0)
scharr_x = cv.convertScaleAbs(scharr_x)
cv.imshow('img', img)
cv.imshow('scharr_x', scharr_x)
cv.waitKey()
cv.destroyAllWindows()
