# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# -----------------读取原始图像----------------------
o = cv.imread('cc.bmp')
cv.imshow("original", o)

# -----------------获取轮廓------------------------
gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
image, contours, hierarchy = cv.findContours(binary,
                                              cv.RETR_LIST,
                                              cv.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

# -----------------绘制空心轮廓------------------------
mask1 = np.zeros(gray.shape, np.uint8)
cv.drawContours(mask1, [cnt], 0, 255, 2)
pixelpoints1 = cv.findNonZero(mask1)
print("pixelpoints1.shape=", pixelpoints1.shape)
print("pixelpoints1=\n", pixelpoints1)
cv.imshow("mask1", mask1)

# -----------------绘制实心轮廓---------------------
mask2 = np.zeros(gray.shape, np.uint8)
cv.drawContours(mask2, [cnt], 0, 255, -1)
pixelpoints2 = cv.findNonZero(mask2)
print("pixelpoints2.shape=", pixelpoints2.shape)
print("pixelpoints2=\n", pixelpoints2)
cv.imshow("mask2", mask2)

# -----------------释放窗口------------------------
cv.waitKey()
cv.destroyAllWindows()
