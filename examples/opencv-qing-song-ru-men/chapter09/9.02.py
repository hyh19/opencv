# -*- coding: utf-8 -*-
import cv2 as cv

img_gray = cv.imread('sobel4.bmp', cv.IMREAD_GRAYSCALE)
sobel_x = cv.Sobel(img_gray, -1, 1, 0)
cv.imshow('gray', img_gray)
cv.imshow('sobel_x', sobel_x)
cv.waitKey()
cv.destroyAllWindows()
