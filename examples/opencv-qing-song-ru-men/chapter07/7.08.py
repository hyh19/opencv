# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('lenaNoise.png')
res = cv.bilateralFilter(img, 25, 100, 100)
cv.imshow('img', img)
cv.imshow('res', res)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/58W7Sj
