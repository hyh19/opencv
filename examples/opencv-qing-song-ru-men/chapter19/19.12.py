# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

win_name = 'win'
trackbar_blue = 'Blue'
trackbar_green = 'Green'
trackbar_red = 'Red'


def change_color(x):
    b = cv.getTrackbarPos(trackbar_blue, win_name)
    g = cv.getTrackbarPos(trackbar_green, win_name)
    r = cv.getTrackbarPos(trackbar_red, win_name)
    img[:] = [b, g, r]


img = np.zeros((100, 700, 3), np.uint8)
cv.namedWindow(win_name)
cv.createTrackbar(trackbar_blue, win_name, 0, 255, change_color)
cv.createTrackbar(trackbar_green, win_name, 0, 255, change_color)
cv.createTrackbar(trackbar_red, win_name, 0, 255, change_color)
while True:
    cv.imshow(win_name, img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()

# 运行结果 https://is.gd/frlSLn
