# -*- coding: utf-8 -*-
import cv2 as cv
import matplotlib.pyplot as plt

o = cv.imread("image/boat.bmp")
plt.hist(o.ravel(), 16)
plt.show()
