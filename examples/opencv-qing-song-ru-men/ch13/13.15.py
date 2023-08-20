# -*- coding: utf-8 -*-
import cv2 as cv
import matplotlib.pyplot as plt

o = cv.imread('image/8.bmp')
g = cv.cvtColor(o, cv.COLOR_BGR2GRAY)
plt.figure("灰度图像显示演示")
plt.subplot(221), plt.imshow(g, cmap=plt.cm.gray)
plt.subplot(222), plt.imshow(g, cmap=plt.cm.gray_r)
plt.subplot(223), plt.imshow(g, cmap='gray')
plt.subplot(224), plt.imshow(g, cmap='gray_r')
plt.show()
