# -*- coding: utf-8 -*-
import cv2 as cv

img_gray = cv.imread('lena.bmp', cv.IMREAD_GRAYSCALE)

img_sobel_x = cv.Sobel(img_gray, ddepth=cv.CV_64F, dx=1, dy=0, ksize=3)
img_sobel_x = cv.convertScaleAbs(img_sobel_x)
img_sobel_y = cv.Sobel(img_gray, ddepth=cv.CV_64F, dx=0, dy=1, ksize=3)
img_sobel_y = cv.convertScaleAbs(img_sobel_y)
img_sobel_xy = cv.addWeighted(img_sobel_x, 0.5, img_sobel_y, 0.5, 0)

img_scharr_x = cv.Scharr(img_gray, ddepth=cv.CV_64F, dx=1, dy=0)
img_scharr_x = cv.convertScaleAbs(img_scharr_x)
img_scharr_y = cv.Scharr(img_gray, ddepth=cv.CV_64F, dx=0, dy=1)
img_scharr_y = cv.convertScaleAbs(img_scharr_y)
img_scharr_xy = cv.addWeighted(img_scharr_x, 0.5, img_scharr_y, 0.5, 0)

cv.imshow('gray', img_gray)
cv.imshow('sobel_xy', img_sobel_xy)
cv.imshow('scharr_xy', img_scharr_xy)

cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/zXvfGJ
