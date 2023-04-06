# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://is.gd/xIzPBH

img = cv.imread('ct.png')
cv.imshow("img", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
_, contours, _ = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
img_contours = img.copy()
cv.drawContours(img_contours, contours, -1, (255, 0, 0), 2)
cv.imshow("img_contours", img_contours)

cnt = contours[2]

# 单通道
mask1 = np.zeros(gray.shape, np.uint8)
mask1 = cv.drawContours(mask1, [cnt], -1, 255, -1)
cv.imshow("mask1", mask1)

gray_mask1 = cv.bitwise_and(gray, mask1)
cv.imshow('gray_mask1', gray_mask1)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(gray, mask=mask1)
print(f'min_val = {min_val}, max_val = {max_val}')
print(f'min_loc = {min_loc}, max_loc = {max_loc}')

# 三通道
mask3 = np.zeros(img.shape, np.uint8)
mask3 = cv.drawContours(mask3, [cnt], -1, (255, 255, 255), -1)
res = cv.bitwise_and(img, mask3)
cv.imshow("res", res)

cv.waitKey()
cv.destroyAllWindows()

'''
min_val = 42.0, max_val = 200.0
min_loc = (87, 90), max_loc = (90, 110)
'''
