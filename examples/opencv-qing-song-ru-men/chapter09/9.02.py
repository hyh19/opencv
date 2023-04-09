# -*- coding: utf-8 -*-
import cv2 as cv

gray_img = cv.imread('sobel4.bmp', cv.IMREAD_GRAYSCALE)
sobel_x_img = cv.Sobel(gray_img, -1, 1, 0)
cv.imshow('gray', gray_img)
cv.imshow('sobel_x', sobel_x_img)
cv.waitKey()
cv.destroyAllWindows()
