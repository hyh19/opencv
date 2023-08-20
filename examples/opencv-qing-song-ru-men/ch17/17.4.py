# -*- coding: utf-8 -*-
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('water_coins.jpg')

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

_, img_bin_inv = cv.threshold(img_gray, thresh=0, maxval=255,
                              type=cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

kernel = np.ones((3, 3), np.uint8)
img_open = cv.morphologyEx(img_bin_inv, cv.MORPH_OPEN, kernel, iterations=2)

img_dilate = cv.dilate(img_open, kernel, iterations=3)

img_dist = cv.distanceTransform(img_open, cv.DIST_L2, 5)
# If the image is 32-bit or 64-bit floating-point, the pixel values are multiplied by 255.
# That is, the value range [0,1] is mapped to [0,255].
img_dist = np.uint8(img_dist)

_, img_fg = cv.threshold(img_dist, thresh=0.7 * img_dist.max(), maxval=255,
                         type=cv.THRESH_BINARY)
img_fg = np.uint8(img_fg)

img_unknown = cv.subtract(img_dilate, img_fg)

count, img_markers = cv.connectedComponents(img_fg)

plt.subplot(121), plt.imshow(img_dist, cmap='gray'), plt.axis('off')
plt.subplot(122), plt.imshow(img_markers, cmap='gray'), plt.axis('off')
plt.show()

cv.imshow('img', img)
cv.imshow('gray', img_gray)
cv.imshow('binary_inv', img_bin_inv)
cv.imshow('open', img_open)
cv.imshow('dilate', img_dilate)
cv.imshow('fg', img_fg)
cv.imshow('unknown', img_unknown)

cv.waitKey()
cv.destroyAllWindows()

# 运行结果
# https://is.gd/PgPNdE
# https://is.gd/3ttvnz
