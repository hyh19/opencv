# -*- coding: utf-8 -*-
import cv2
import numpy as np


def change_color(x):
    r = cv2.getTrackbarPos('R', 'win')
    g = cv2.getTrackbarPos('G', 'win')
    b = cv2.getTrackbarPos('B', 'win')
    img[:] = [b, g, r]


img = np.zeros((100, 700, 3), np.uint8)
cv2.namedWindow('win')
cv2.createTrackbar('R', 'win', 0, 255, change_color)
cv2.createTrackbar('G', 'win', 0, 255, change_color)
cv2.createTrackbar('B', 'win', 0, 255, change_color)
while True:
    cv2.imshow('win', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()

# 运行结果 https://is.gd/frlSLn
