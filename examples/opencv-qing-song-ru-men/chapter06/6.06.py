# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('lena.bmp')
thresh, res = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
cv.imshow('img', img)
cv.imshow('res', res)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/uWHAjn
