# -*- coding: utf-8 -*-
import cv2 as cv

img_gray = cv.imread('scharr.bmp', cv.IMREAD_GRAYSCALE)
img_scharr_x = cv.Scharr(img_gray, cv.CV_64F, 1, 0)
img_scharr_x = cv.convertScaleAbs(img_scharr_x)
cv.imshow('gray', img_gray)
cv.imshow('scharr_x', img_scharr_x)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/mUSszp
