# -*- coding: utf-8 -*-
import cv2 as cv

img_gray = cv.imread('sobel4.bmp', cv.IMREAD_GRAYSCALE)
img_sobel_y = cv.Sobel(img_gray, ddepth=cv.CV_64F, dx=0, dy=1)
img_sobel_y = cv.convertScaleAbs(img_sobel_y)
cv.imshow('gray', img_gray)
cv.imshow('sobel_y', img_sobel_y)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/eQWFfh
