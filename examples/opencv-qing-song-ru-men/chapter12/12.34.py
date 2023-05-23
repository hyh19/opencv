# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread('cc.bmp')
cv.imshow("img", img)

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, img_binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)
_, contours, _ = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

# 绘制空心轮廓
mask1 = np.zeros(img_gray.shape, np.uint8)
cv.drawContours(mask1, [cnt], 0, 255, 2)
cv.imshow("mask1", mask1)

# 绘制实心轮廓
mask2 = np.zeros(img_gray.shape, np.uint8)
cv.drawContours(mask2, [cnt], 0, 255, -1)
cv.imshow("mask2", mask2)

cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/niHjZ3
