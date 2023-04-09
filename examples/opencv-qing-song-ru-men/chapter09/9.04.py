# -*- coding: utf-8 -*-
import cv2 as cv

gray_img = cv.imread('sobel4.bmp', cv.IMREAD_GRAYSCALE)
sobel_y_img = cv.Sobel(gray_img, cv.CV_64F, 0, 1)
sobel_y_img = cv.convertScaleAbs(sobel_y_img)
cv.imshow('gray', gray_img)
cv.imshow('sobel_y', sobel_y_img)
cv.waitKey()
cv.destroyAllWindows()
