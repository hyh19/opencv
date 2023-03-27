# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=[4, 5], dtype=np.uint8)
thresh, res = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
print("img=\n", img)
print("thresh=", thresh)
print("res=\n", res)

"""
img=
 [[ 81 218 240  66 225]
 [ 59   8 114   0 204]
 [251 220 199 101  37]
 [172  67  18 219 121]]
thresh= 127.0
res=
 [[255   0   0 255   0]
 [255 255 255 255   0]
 [  0   0   0 255 255]
 [  0 255 255   0 255]]
"""
