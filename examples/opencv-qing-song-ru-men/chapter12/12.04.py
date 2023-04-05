# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://is.gd/LzXi5z

img = cv.imread('moments.bmp')
cv.imshow("img", img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
_, contours, hierarchy = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
n = len(contours)
for i in range(n):
    temp = np.zeros(img.shape, np.uint8)
    cv.drawContours(temp, contours, i, (255, 255, 255), 3)
    cv.imshow(f'contours[{i}]', temp)

    moments = cv.moments(contours[i])
    print(f'轮廓 {i} 的矩: {moments}')
    m00 = moments["m00"]
    print(f'轮廓 {i} 的面积: {m00}')
cv.waitKey()
cv.destroyAllWindows()
