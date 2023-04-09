# -*- coding: utf-8 -*-
import cv2 as cv

gray_img = cv.imread('sobel4.bmp', cv.IMREAD_GRAYSCALE)
sobel_xy_img = cv.Sobel(gray_img, cv.CV_64F, 1, 1)
sobel_xy_img = cv.convertScaleAbs(sobel_xy_img)
cv.imshow('gray', gray_img)
cv.imshow('sobel_xy', sobel_xy_img)
cv.waitKey()
cv.destroyAllWindows()
