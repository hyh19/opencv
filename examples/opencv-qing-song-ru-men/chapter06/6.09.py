# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=[4, 5], dtype=np.uint8)
thresh, res = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
print('img=\n', img)
print('thresh=', thresh)
print('res=\n', res)

'''
img=
 [[122  34  89 245  86]
 [ 75 205 144 100 192]
 [136 131 138  99  34]
 [158  31  75 134  75]]
thresh= 127.0
res=
 [[  0   0   0 245   0]
 [  0 205 144   0 192]
 [136 131 138   0   0]
 [158   0   0 134   0]]
'''
