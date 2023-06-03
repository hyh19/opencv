# -*- coding: utf-8 -*-
import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('water_coins.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, img_bin_inv = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
kernel = np.ones((3, 3), np.uint8)
img_open = cv2.morphologyEx(img_bin_inv, cv2.MORPH_OPEN, kernel, iterations=2)

img_dist = cv2.distanceTransform(img_open, cv2.DIST_L2, 5)
_, img_fg = cv2.threshold(img_dist, 0.7 * img_dist.max(), 255, cv2.THRESH_BINARY)

plt.subplot(131), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.axis('off')
plt.subplot(132), plt.imshow(img_dist, cmap='gray'), plt.axis('off')
plt.subplot(133), plt.imshow(img_fg, cmap='gray'), plt.axis('off')
plt.show()

# 运行结果 https://is.gd/e5bl4J
