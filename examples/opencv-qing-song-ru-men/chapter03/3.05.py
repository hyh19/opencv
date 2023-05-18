# -*- coding: utf-8 -*-
import cv2 as cv

boat = cv.imread('boat.bmp')
lena = cv.imread('lena.bmp')
result = cv.addWeighted(boat, 0.6, lena, 0.4, 0)
cv.imshow('boat', boat)
cv.imshow('lena', lena)
cv.imshow('result', result)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/CRt5AO
