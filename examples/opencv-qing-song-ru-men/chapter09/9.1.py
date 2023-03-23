# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

a = np.random.randint(-256, 256, size=[4, 5], dtype=np.int16)
# https://bit.ly/3lDpvuX
res = cv.convertScaleAbs(a)
print("a=\n", a)
print("res=\n", res)
