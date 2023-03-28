# -*- coding: utf-8 -*-
import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('water_coins.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, binary_inv = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

kernel = np.ones((3, 3), np.uint8)
open1 = cv2.morphologyEx(binary_inv, cv2.MORPH_OPEN, kernel, iterations=2)

dist = cv2.distanceTransform(open1, cv2.DIST_L2, 5)
_, fg = cv2.threshold(dist, 0.7 * dist.max(), 255, cv2.THRESH_BINARY)

plt.subplot(131), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.axis('off')
plt.subplot(132), plt.imshow(dist, cmap='gray'), plt.axis('off')
plt.subplot(133), plt.imshow(fg, cmap='gray'), plt.axis('off')
plt.show()
