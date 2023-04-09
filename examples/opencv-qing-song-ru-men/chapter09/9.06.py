# -*- coding: utf-8 -*-
import cv2 as cv

gray_img = cv.imread('sobel4.bmp', cv.IMREAD_GRAYSCALE)

sobel_x_img = cv.Sobel(gray_img, cv.CV_64F, 1, 0)
sobel_x_img = cv.convertScaleAbs(sobel_x_img)

sobel_y_img = cv.Sobel(gray_img, cv.CV_64F, 0, 1)
sobel_y_img = cv.convertScaleAbs(sobel_y_img)

sobel_xy_img = cv.addWeighted(sobel_x_img, 0.5, sobel_y_img, 0.5, 0)

cv.imshow('gray', gray_img)
cv.imshow('sobel_x', sobel_x_img)
cv.imshow('sobel_y', sobel_y_img)
cv.imshow('sobel_xy', sobel_xy_img)

cv.waitKey()
cv.destroyAllWindows()
