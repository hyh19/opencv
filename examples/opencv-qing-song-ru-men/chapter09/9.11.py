# -*- coding: utf-8 -*-
import cv2 as cv

img_gray = cv.imread('scharr.bmp', cv.IMREAD_GRAYSCALE)
scharr_xy = cv.Scharr(img_gray, cv.CV_64F, 1, 1)
cv.imshow('img_gray', img_gray)
cv.imshow('scharr_xy', scharr_xy)
cv.waitKey()
cv.destroyAllWindows()
