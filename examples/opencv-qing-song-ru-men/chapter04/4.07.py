# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=[5, 5], dtype=np.uint8)
mask = cv.inRange(img, 100, 200)
print('img=\n', img)
print('mask=\n', mask)

'''
img=
 [[142 217 166 164  80]
 [109 230  27  60  25]
 [201 204   2  89  98]
 [202 204 198 253  66]
 [ 20  33  14 189 188]]
mask=
 [[255   0 255 255   0]
 [255   0   0   0   0]
 [  0   0   0   0   0]
 [  0   0 255   0   0]
 [  0   0   0 255 255]]
'''
