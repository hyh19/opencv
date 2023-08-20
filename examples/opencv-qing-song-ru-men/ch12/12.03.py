# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread('loc3.jpg')
cv.imshow("img", img)

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", img_gray)

_, img_binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)
cv.imshow("binary", img_binary)

_, contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
mask = np.zeros(img.shape, np.uint8)
mask = cv.drawContours(mask, contours, -1, (255, 255, 255), -1)
cv.imshow("mask", mask)

fg = cv.bitwise_and(img, mask)
cv.imshow("fg", fg)

cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/ZWzDrn
