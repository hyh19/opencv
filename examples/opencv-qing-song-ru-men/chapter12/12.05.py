# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://is.gd/oQZZPp

img = cv.imread('contours.bmp')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
_, contours, hierarchy = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.imshow("img", img)
for i in range(len(contours)):
    temp = np.zeros(img.shape, np.uint8)
    cv.drawContours(temp, contours, i, (255, 255, 255), 3)
    cv.imshow(f'contours[{i}]', temp)
    print(f'contours[{i}] 的面积 = {cv.contourArea(contours[i])}')
cv.waitKey()
cv.destroyAllWindows()
