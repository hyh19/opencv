# -*- coding: utf-8 -*-
import cv2 as cv

img_gray = cv.imread('sobel4.bmp', cv.IMREAD_GRAYSCALE)
img_sobel_x = cv.Sobel(img_gray, ddepth=-1, dx=1, dy=0)
cv.imshow('gray', img_gray)
cv.imshow('sobel_x', img_sobel_x)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/HF7qu2
