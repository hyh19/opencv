# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=[4, 5], dtype=np.uint8)
t, rst = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
print("img=\n", img)
print("t=", t)
print("rst=\n", rst)
