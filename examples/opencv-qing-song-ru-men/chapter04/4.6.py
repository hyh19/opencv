# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# =========测试下OpenCV中蓝色的HSV模式值=============
imgBlue = np.zeros([1, 1, 3], dtype=np.uint8)
imgBlue[0, 0, 0] = 255
Blue = imgBlue
BlueHSV = cv.cvtColor(Blue, cv.COLOR_BGR2HSV)
print("Blue=\n", Blue)
print("BlueHSV=\n", BlueHSV)
# =========测试下OpenCV中绿色的HSV模式值=============
imgGreen = np.zeros([1, 1, 3], dtype=np.uint8)
imgGreen[0, 0, 1] = 255
Green = imgGreen
GreenHSV = cv.cvtColor(Green, cv.COLOR_BGR2HSV)
print("Green=\n", Green)
print("GreenHSV=\n", GreenHSV)
# =========测试下OpenCV中红色的HSV模式值=============
imgRed = np.zeros([1, 1, 3], dtype=np.uint8)
imgRed[0, 0, 2] = 255
Red = imgRed
RedHSV = cv.cvtColor(Red, cv.COLOR_BGR2HSV)
print("Red=\n", Red)
print("RedHSV=\n", RedHSV)
