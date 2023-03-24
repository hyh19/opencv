# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('sobel4.bmp', cv.IMREAD_GRAYSCALE)
sobel_x = cv.Sobel(img, -1, 1, 0)
cv.imshow('img', img)
cv.imshow('sobel_x', sobel_x)
cv.waitKey()
cv.destroyAllWindows()
