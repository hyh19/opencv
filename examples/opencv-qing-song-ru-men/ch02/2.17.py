# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://is.gd/iAwQwb

lena = cv.imread('lenacolor.png')
blue, green, red = cv.split(lena)
cv.imshow('lena', lena)
cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)
cv.waitKey()
cv.destroyAllWindows()
