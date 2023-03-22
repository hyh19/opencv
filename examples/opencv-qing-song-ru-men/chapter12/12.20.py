# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread('contours.bmp')
gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
image, contours, hierarchy = cv.findContours(binary,
                                              cv.RETR_TREE,
                                              cv.CHAIN_APPROX_SIMPLE)
hull = cv.convexHull(contours[0])  # 返回坐标值
print("returnPoints为默认值True时返回值hull的值：\n", hull)
hull2 = cv.convexHull(contours[0], returnPoints=False)  # 返回索引值
print("returnPoints为False时返回值hull的值：\n", hull2)
