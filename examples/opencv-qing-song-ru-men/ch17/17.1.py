# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("rice.png")
kernel = np.ones((5, 5), np.uint8)
img_erode = cv.erode(img, kernel)
img_subtract = cv.subtract(img, img_erode)
plt.subplot(131), plt.imshow(img), plt.axis('off')
plt.subplot(132), plt.imshow(img_erode), plt.axis('off')
plt.subplot(133), plt.imshow(img_subtract), plt.axis('off')
plt.show()

# 运行结果 https://is.gd/kEXNv7
