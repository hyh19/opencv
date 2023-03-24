# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('sobel4.bmp', cv.IMREAD_GRAYSCALE)
sobel_y = cv.Sobel(img, cv.CV_64F, 0, 1)
sobel_y = cv.convertScaleAbs(sobel_y)
cv.imshow('img', img)
cv.imshow('sobel_y', sobel_y)
cv.waitKey()
cv.destroyAllWindows()
