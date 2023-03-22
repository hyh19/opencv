# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(-256, 256, size=[4, 5], dtype=np.int16)
rst = cv.convertScaleAbs(img)
print("img=\n", img)
print("rst=\n", rst)
