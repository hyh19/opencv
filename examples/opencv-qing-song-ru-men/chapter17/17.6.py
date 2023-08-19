# -*- coding: utf-8 -*-
import numpy as np
import cv2 as cv as cv
import matplotlib.pyplot as plt

img = cv.imread('water_coins.jpg')
cv.imshow('img', img)

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', img_gray)

_, img_binary_inv = cv.threshold(img_gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
cv.imshow('binary_inv', img_binary_inv)

kernel = np.ones((3, 3), np.uint8)
img_open = cv.morphologyEx(img_binary_inv, cv.MORPH_OPEN, kernel, iterations=2)
cv.imshow('open', img_open)

img_dilate = cv.dilate(img_open, kernel, iterations=3)
cv.imshow('dilate', img_dilate)

img_dist = cv.distanceTransform(img_open, cv.DIST_L2, 5)
plt.imshow(img_dist, cmap='gray')
plt.show()

_, img_fg = cv.threshold(img_dist, 0.7 * img_dist.max(), 255, cv.THRESH_BINARY)
cv.imshow('fg', img_fg)

img_fg = np.uint8(img_fg)
img_unknown = cv.subtract(img_dilate, img_fg)
cv.imshow('unknown', img_unknown)

count, markers = cv.connectedComponents(img_fg)
markers = markers + 1
markers[img_unknown == 255] = 0

markers = cv.watershed(img, markers)
img[markers == -1] = [0, 0, 255]
cv.imshow('result', img)

cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/BIY0ss
