# -*- coding: utf-8 -*-
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('image/equ.bmp', cv.IMREAD_GRAYSCALE)
equ = cv.equalizeHist(img)
plt.figure("subplot示例")
plt.subplot(121), plt.hist(img.ravel(), 256)
plt.subplot(122), plt.hist(equ.ravel(), 256)
plt.show()
