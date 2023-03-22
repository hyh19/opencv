# -*- coding: utf-8 -*-
import cv2
import matplotlib.pyplot as plt

o = cv2.imread('image/girl.bmp')
g = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
plt.figure("灰度图像显示演示")
plt.subplot(221), plt.imshow(o), plt.axis('off')
plt.subplot(222), plt.imshow(o, cmap=plt.cm.gray), plt.axis('off')
plt.subplot(223), plt.imshow(g), plt.axis('off')
plt.subplot(224), plt.imshow(g, cmap=plt.cm.gray), plt.axis('off')
plt.show()
