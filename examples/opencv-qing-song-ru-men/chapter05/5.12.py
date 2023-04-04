# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=[4, 5], dtype=np.uint8)
row_size, col_size = img.shape
map_row = np.zeros(img.shape, np.float32)
map_col = np.zeros(img.shape, np.float32)

for row in range(row_size):
    for col in range(col_size):
        map_row.itemset((row, col), row_size - 1 - row)
        map_col.itemset((row, col), col)

res = cv.remap(img, map_col, map_row, cv.INTER_LINEAR)
print('img=\n', img)
print('map_row=\n', map_row)
print('map_col=\n', map_col)
print('res=\n', res)

'''
img=
 [[138 123   5  57  53]
 [227 174 106   9  66]
 [ 75 137 159 171  37]
 [ 95 161 116 133 122]]
map_row=
 [[3. 3. 3. 3. 3.]
 [2. 2. 2. 2. 2.]
 [1. 1. 1. 1. 1.]
 [0. 0. 0. 0. 0.]]
map_col=
 [[0. 1. 2. 3. 4.]
 [0. 1. 2. 3. 4.]
 [0. 1. 2. 3. 4.]
 [0. 1. 2. 3. 4.]]
res=
 [[ 95 161 116 133 122]
 [ 75 137 159 171  37]
 [227 174 106   9  66]
 [138 123   5  57  53]]
'''
