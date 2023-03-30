# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 运行结果 https://is.gd/u6WHFZ

size = 300
blue = (255, 0, 0)
green = (0, 255, 0)
red = (0, 0, 255)

img = np.zeros((size + 1, size + 1, 3), np.uint8)
img = cv2.line(img, (0, 0), (size, size), blue, 3)
img = cv2.line(img, (0, 100), (size, 100), green, 1)
img = cv2.line(img, (100, 0), (100, size), red, 6)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
