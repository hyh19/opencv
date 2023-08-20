# -*- coding: utf-8 -*-
import cv2 as cv

img_gray = cv.imread('sobel4.bmp', cv.IMREAD_GRAYSCALE)

img_sobel_x = cv.Sobel(img_gray, cv.CV_64F, 1, 0)
img_sobel_x = cv.convertScaleAbs(img_sobel_x)

img_sobel_y = cv.Sobel(img_gray, cv.CV_64F, 0, 1)
img_sobel_y = cv.convertScaleAbs(img_sobel_y)

img_sobel_xy = cv.addWeighted(img_sobel_x, 0.5, img_sobel_y, 0.5, 0)

cv.imshow('gray', img_gray)
cv.imshow('sobel_x', img_sobel_x)
cv.imshow('sobel_y', img_sobel_y)
cv.imshow('sobel_xy', img_sobel_xy)

cv.waitKey()
cv.destroyAllWindows()
