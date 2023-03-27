# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=[4, 5], dtype=np.uint8)
thresh, res = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
print("img=\n", img)
print("thresh=", thresh)
print("res=\n", res)

"""
img=
 [[139  19  90 108  49]
 [140 157 211 209  26]
 [ 87  70 100 211  62]
 [109  35 196  11  97]]
thresh= 127.0
res=
 [[127  19  90 108  49]
 [127 127 127 127  26]
 [ 87  70 100 127  62]
 [109  35 127  11  97]]
"""
