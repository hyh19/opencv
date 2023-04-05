# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://is.gd/5BJsHl

img = cv.imread('contours.bmp')
cv.imshow("img", img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
_, contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    temp = np.zeros(img.shape, np.uint8)
    cv.drawContours(temp, contours, i, (255, 255, 255), 5)
    cv.imshow(f'contours[{i}]', temp)
cv.waitKey()
cv.destroyAllWindows()
