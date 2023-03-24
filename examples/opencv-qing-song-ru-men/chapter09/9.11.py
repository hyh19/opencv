# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('scharr.bmp', cv.IMREAD_GRAYSCALE)
scharr_xy = cv.Scharr(img, cv.CV_64F, 1, 1)
cv.imshow('img', img)
cv.imshow('scharr_xy', scharr_xy)
cv.waitKey()
cv.destroyAllWindows()
