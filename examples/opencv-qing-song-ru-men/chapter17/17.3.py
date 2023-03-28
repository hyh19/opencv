# -*- coding: utf-8 -*-
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 运行结果 https://is.gd/3ttvnz

img = cv.imread('water_coins.jpg')
cv.imshow('img', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

_, binary_inv = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
cv.imshow('binary_inv', binary_inv)

kernel = np.ones((3, 3), np.uint8)
open1 = cv.morphologyEx(binary_inv, cv.MORPH_OPEN, kernel, iterations=2)
cv.imshow('open', open1)

dilate = cv.dilate(open1, kernel, iterations=3)
cv.imshow('dilate', dilate)

dist = cv.distanceTransform(open1, cv.DIST_L2, 5)
plt.imshow(dist, cmap='gray')
plt.show()

_, fg = cv.threshold(dist, 0.7 * dist.max(), 255, cv.THRESH_BINARY)
cv.imshow('fg', fg)

fg = np.uint8(fg)
unknown = cv.subtract(dilate, fg)
cv.imshow('unknown', unknown)

cv.waitKey()
cv.destroyAllWindows()
