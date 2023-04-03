# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img1 = np.ones((4, 4), dtype=np.uint8) * 3
img2 = np.ones((4, 4), dtype=np.uint8) * 5
mask = np.zeros((4, 4), dtype=np.uint8)
mask[2:4, 2:4] = 1
result = cv.add(img1, img2, mask=mask)
print('img1=\n', img1)
print('img2=\n', img2)
print('mask=\n', mask)
print('result=\n', result)

'''
img1=
 [[3 3 3 3]
 [3 3 3 3]
 [3 3 3 3]
 [3 3 3 3]]
img2=
 [[5 5 5 5]
 [5 5 5 5]
 [5 5 5 5]
 [5 5 5 5]]
mask=
 [[0 0 0 0]
 [0 0 0 0]
 [0 0 1 1]
 [0 0 1 1]]
result=
 [[0 0 0 0]
 [0 0 0 0]
 [0 0 8 8]
 [0 0 8 8]]
'''
