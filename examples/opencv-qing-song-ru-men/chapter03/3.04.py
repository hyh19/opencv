# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img1 = np.ones((3, 4), dtype=np.uint8) * 100
img2 = np.ones((3, 4), dtype=np.uint8) * 10
gamma = 3
img3 = cv.addWeighted(img1, 0.6, img2, 5, gamma)
print(img3)
