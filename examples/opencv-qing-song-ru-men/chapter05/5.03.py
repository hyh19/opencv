# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread("test.bmp")
rst = cv.resize(img, None, fx=2, fy=0.5)
print("img.shape=", img.shape)
print("rst.shape=", rst.shape)
