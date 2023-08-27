# -*- coding: utf-8 -*-
import cv2 as cv

img_gray = cv.imread('Laplacian.bmp', cv.IMREAD_GRAYSCALE)
img_laplacian = cv.Laplacian(img_gray, ddepth=cv.CV_64F)
img_laplacian = cv.convertScaleAbs(img_laplacian)
cv.imshow('gray', img_gray)
cv.imshow('laplacian', img_laplacian)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/RehhTt
