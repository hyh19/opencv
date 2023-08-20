# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://is.gd/KFiXK8

lena = cv.imread('lenacolor.png')
blue, green, red = cv.split(lena)
bgr = cv.merge([blue, green, red])
rgb = cv.merge([red, green, blue])
cv.imshow('lena', lena)
cv.imshow('bgr', bgr)
cv.imshow('rgb', rgb)
cv.waitKey()
cv.destroyAllWindows()
