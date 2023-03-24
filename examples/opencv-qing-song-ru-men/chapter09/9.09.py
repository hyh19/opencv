# -*- coding: utf-8 -*-
import cv2 as cv

img_gray = cv.imread('scharr.bmp', cv.IMREAD_GRAYSCALE)
scharr_y = cv.Scharr(img_gray, cv.CV_64F, 0, 1)
scharr_y = cv.convertScaleAbs(scharr_y)
cv.imshow('img_gray', img_gray)
cv.imshow('scharr_y', scharr_y)
cv.waitKey()
cv.destroyAllWindows()
