# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = np.zeros((5, 5), np.uint8)
img[1:4, 1:4] = 1
kernel = np.ones((3, 1), np.uint8)
erosion = cv2.erode(img, kernel)
print("img=\n", img)
print("kernel=\n", kernel)
print("erosion=\n", erosion)
