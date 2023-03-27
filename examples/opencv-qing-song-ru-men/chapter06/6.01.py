# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=[4, 5], dtype=np.uint8)
thresh, res = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
print("img=\n", img)
print("thresh=", thresh)
print("res=\n", res)

"""
img=
 [[ 36  47 123 141 245]
 [ 69 226  24 171  44]
 [246  58 252  92  28]
 [  0 197 239 146 203]]
thresh= 127.0
res=
 [[  0   0   0 255 255]
 [  0 255   0 255   0]
 [255   0 255   0   0]
 [  0 255 255 255 255]]
"""
