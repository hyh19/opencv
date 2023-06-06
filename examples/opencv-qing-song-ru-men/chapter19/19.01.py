# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

size = 300
blue = (255, 0, 0)
green = (0, 255, 0)
red = (0, 0, 255)

img = np.zeros((size + 1, size + 1, 3), np.uint8)
cv.line(img, (0, 0), (size, size), blue, 3)
cv.line(img, (0, 100), (size, 100), green, 1)
cv.line(img, (100, 0), (100, size), red, 6)

cv.imshow('img', img)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/u6WHFZ
