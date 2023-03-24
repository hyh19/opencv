# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.zeros((5, 5), np.uint8)
img[2:3, 1:4] = 1
kernel = np.ones((3, 1), np.uint8)
dilate = cv.dilate(img, kernel)
print('img=\n', img)
print('kernel=\n', kernel)
print('dilate\n', dilate)
