# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread("image/lena.bmp")
hist = cv.calcHist([img], [0], None, [256], [0, 255])
print(type(hist))
print(hist.shape)
print(hist.size)
print(hist)
