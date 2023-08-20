# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread('contours.bmp')
cv.imshow("img", img)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, img_binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)
_, contours, hierarchy = cv.findContours(img_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    canvas = np.zeros(img.shape, np.uint8)
    cv.drawContours(canvas, contours, i, (255, 255, 255), 5)
    cv.imshow(f'contours[{i}]', canvas)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/5BJsHl
