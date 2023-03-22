# -*- coding: utf-8 -*-
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image/girl.bmp')
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure("显示结果")
plt.subplot(121), plt.imshow(img), plt.axis('off')
plt.subplot(122), plt.imshow(imgRGB), plt.axis('off')
plt.show()
