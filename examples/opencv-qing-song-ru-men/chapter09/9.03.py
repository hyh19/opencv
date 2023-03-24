# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('sobel4.bmp', cv.IMREAD_GRAYSCALE)
sobel_x = cv.Sobel(img, cv.CV_64F, 1, 0)
sobel_x = cv.convertScaleAbs(sobel_x)
cv.imshow('img', img)
cv.imshow('sobel_x', sobel_x)
cv.waitKey()
cv.destroyAllWindows()
