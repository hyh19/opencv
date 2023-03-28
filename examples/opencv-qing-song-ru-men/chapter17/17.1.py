# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("rice.png", cv2.IMREAD_UNCHANGED)
kernel = np.ones((5, 5), np.uint8)
erode = cv2.erode(img, kernel)
subtract = cv2.subtract(img, erode)
plt.subplot(131), plt.imshow(img), plt.axis('off')
plt.subplot(132), plt.imshow(erode), plt.axis('off')
plt.subplot(133), plt.imshow(subtract), plt.axis('off')
plt.show()
