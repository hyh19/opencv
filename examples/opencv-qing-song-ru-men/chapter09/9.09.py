# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('scharr.bmp', cv.IMREAD_GRAYSCALE)
scharr_y = cv.Scharr(img, cv.CV_64F, 0, 1)
scharr_y = cv.convertScaleAbs(scharr_y)
cv.imshow('img', img)
cv.imshow('scharr_y', scharr_y)
cv.waitKey()
cv.destroyAllWindows()
