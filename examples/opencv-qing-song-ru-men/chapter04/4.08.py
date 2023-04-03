# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.ones([5, 5], dtype=np.uint8) * 9
mask = np.zeros([5, 5], dtype=np.uint8)
mask[0:3, 0] = 1
mask[2:5, 2:4] = 1
roi = cv.bitwise_and(img, img, mask=mask)
print('img=\n', img)
print('mask=\n', mask)
print('roi=\n', roi)

'''
img=
 [[9 9 9 9 9]
 [9 9 9 9 9]
 [9 9 9 9 9]
 [9 9 9 9 9]
 [9 9 9 9 9]]
mask=
 [[1 0 0 0 0]
 [1 0 0 0 0]
 [1 0 1 1 0]
 [0 0 1 1 0]
 [0 0 1 1 0]]
roi=
 [[9 0 0 0 0]
 [9 0 0 0 0]
 [9 0 9 9 0]
 [0 0 9 9 0]
 [0 0 9 9 0]]
'''
