# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=[4, 5], dtype=np.uint8)
thresh, res = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)
print('img=\n', img)
print('thresh=', thresh)
print('res=\n', res)

'''
img=
 [[  1 200  96 143  26]
 [131  60  43  88 102]
 [ 48 165  51  80 150]
 [ 80 116 217 185 233]]
thresh= 127.0
res=
 [[  1   0  96   0  26]
 [  0  60  43  88 102]
 [ 48   0  51  80   0]
 [ 80 116   0   0   0]]
'''
