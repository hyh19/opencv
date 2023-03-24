# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('sobel4.bmp', cv.IMREAD_GRAYSCALE)
sobel_xy = cv.Sobel(img, cv.CV_64F, 1, 1)
sobel_xy = cv.convertScaleAbs(sobel_xy)
cv.imshow('img', img)
cv.imshow('sobel_xy', sobel_xy)
cv.waitKey()
cv.destroyAllWindows()
