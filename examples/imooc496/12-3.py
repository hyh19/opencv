import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 运行结果 https://is.gd/nfLHXA

img = cv.imread('water_coins.jpeg')
cv.imshow('img', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

_, binary_inv = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
cv.imshow('binary_inv', binary_inv)

kernel = np.ones((3, 3), np.int8)
open1 = cv.morphologyEx(binary_inv, cv.MORPH_OPEN, kernel, iterations=2)
cv.imshow('open', open1)

dilate = cv.dilate(open1, kernel, iterations=1)
cv.imshow('dilate', dilate)

dist = cv.distanceTransform(open1, cv.DIST_L2, 5)
# If the image is 32-bit or 64-bit floating-point, the pixel values are multiplied by 255.
# That is, the value range [0,1] is mapped to [0,255].
# cv.imshow('dist', dist)
plt.imshow(dist, cmap='gray')
plt.show()

_, fg = cv.threshold(dist, 0.7 * dist.max(), 255, cv.THRESH_BINARY)
cv.imshow('fg', fg)

fg = np.uint8(fg)
unknown = cv.subtract(dilate, fg)
cv.imshow('unknown', unknown)

count, markers = cv.connectedComponents(fg)
markers = markers + 1
markers[unknown == 255] = 0

markers = cv.watershed(img, markers)
img[markers == -1] = [0, 0, 255]
cv.imshow('result', img)

cv.waitKey()
cv.destroyAllWindows()
