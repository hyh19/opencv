# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena4.bmp', cv2.IMREAD_GRAYSCALE)
template = cv2.imread('lena4Temp.bmp', 0)
tw, th = template.shape[::-1]

res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + tw, pt[1] + th), 255, 1)

plt.imshow(img, cmap='gray')
plt.xticks([]), plt.yticks([])
plt.show()