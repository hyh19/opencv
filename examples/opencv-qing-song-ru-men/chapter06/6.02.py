# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('lena.bmp')
_, res = cv.threshold(img, thresh=127, maxval=255, type=cv.THRESH_BINARY)
cv.imshow('img', img)
cv.imshow('res', res)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/AOjowe
