# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img1 = np.ones((4, 4), dtype=np.uint8) * 3
img2 = np.ones((4, 4), dtype=np.uint8) * 5
img3 = np.ones((4, 4), dtype=np.uint8) * 66
mask = np.zeros((4, 4), dtype=np.uint8)
mask[2:4, 2:4] = 1
print('img1=\n', img1)
print('img2=\n', img2)
print('img3=\n', img3)
print('mask=\n', mask)
img3 = cv.add(img1, img2, mask=mask)
print('求和后img3=\n', img3)

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
img3=
 [[66 66 66 66]
 [66 66 66 66]
 [66 66 66 66]
 [66 66 66 66]]
mask=
 [[0 0 0 0]
 [0 0 0 0]
 [0 0 1 1]
 [0 0 1 1]]
求和后img3=
 [[0 0 0 0]
 [0 0 0 0]
 [0 0 8 8]
 [0 0 8 8]]
'''
