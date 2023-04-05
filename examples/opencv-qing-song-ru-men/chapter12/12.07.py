# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://is.gd/huaA7o

img = cv.imread('contours0.bmp')
cv.imshow("img", img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
_, contours, hierarchy = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    temp = np.zeros(img.shape, np.uint8)
    cv.drawContours(temp, contours, i, (255, 255, 255), 3)
    cv.imshow(f'contours[{i}]', temp)
    print(f'contours[{i}] 的长度 = {cv.arcLength(contours[i], True)}')
cv.waitKey()
cv.destroyAllWindows()

'''
contours[0] 的长度 = 145.65685415267944
contours[1] 的长度 = 147.65685415267944
contours[2] 的长度 = 398.0
contours[3] 的长度 = 681.6568541526794
contours[4] 的长度 = 1004.0
contours[5] 的长度 = 398.0
contours[6] 的长度 = 681.6568541526794
contours[7] 的长度 = 1004.0
contours[8] 的长度 = 2225.6568541526794
contours[9] 的长度 = 2794.0
'''
