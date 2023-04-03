# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 255, (5, 5), dtype=np.uint8)
mask = np.zeros((5, 5), dtype=np.uint8)
mask[0:3, 0:3] = 255
mask[4, 4] = 255
result = cv.bitwise_and(img, mask)
print('img=\n', img)
print('mask=\n', mask)
print('result=\n', result)

'''
img=
 [[233 241 152 193 133]
 [  8  56  59  51  29]
 [109  44 126  13   0]
 [227 146 247  81 221]
 [ 60  79 111   7 147]]
mask=
 [[255 255 255   0   0]
 [255 255 255   0   0]
 [255 255 255   0   0]
 [  0   0   0   0   0]
 [  0   0   0   0 255]]
result=
 [[233 241 152   0   0]
 [  8  56  59   0   0]
 [109  44 126   0   0]
 [  0   0   0   0   0]
 [  0   0   0   0 147]]
'''
