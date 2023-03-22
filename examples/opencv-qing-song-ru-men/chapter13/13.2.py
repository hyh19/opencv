# -*- coding: utf-8 -*-
import cv2
import matplotlib.pyplot as plt

o = cv2.imread("image/boat.bmp")
plt.hist(o.ravel(), 16)
plt.show()
