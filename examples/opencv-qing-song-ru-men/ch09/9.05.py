# -*- coding: utf-8 -*-
import cv2 as cv

img_gray = cv.imread('sobel4.bmp', cv.IMREAD_GRAYSCALE)
img_sobel_xy = cv.Sobel(img_gray, ddepth=cv.CV_64F, dx=1, dy=1)
img_sobel_xy = cv.convertScaleAbs(img_sobel_xy)
cv.imshow('gray', img_gray)
cv.imshow('sobel_xy', img_sobel_xy)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/sZlWcv
