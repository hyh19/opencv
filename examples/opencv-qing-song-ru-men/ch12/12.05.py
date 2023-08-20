# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread('contours.bmp')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, img_binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)
_, contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.imshow("img", img)
for i in range(len(contours)):
    canvas = np.zeros(img.shape, np.uint8)
    cv.drawContours(canvas, contours, i, (255, 255, 255), 3)
    cv.imshow(f'contours[{i}]', canvas)
    print(f'contours[{i}] 的面积 = {cv.contourArea(contours[i])}')
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/oQZZPp

'''
contours[0] 的面积 = 13108.0
contours[1] 的面积 = 19535.0
contours[2] 的面积 = 12058.0
'''
