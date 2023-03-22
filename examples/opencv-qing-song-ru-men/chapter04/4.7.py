# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=[5, 5], dtype=np.uint8)
lo = 100
up = 200
mask = cv.inRange(img, lo, up)
print("img=\n", img)
print("mask=\n", mask)
