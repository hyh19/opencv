# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread('cc.bmp')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, img_binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)
_, contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

rect = cv.minAreaRect(contours[0])
print(f'rect = {rect}')
points = cv.boxPoints(rect)
print(f'points = \n{points}')
points = np.intp(points)

cv.drawContours(img, contours, 0, (0, 0, 255), 2)
cv.drawContours(img, [points], 0, (255, 0, 0), 2)

cv.imshow("result", img)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/OgchNc
