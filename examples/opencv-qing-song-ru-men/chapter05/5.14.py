# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=[4, 5], dtype=np.uint8)
row_size, col_size = img.shape
map_row = np.zeros(img.shape, np.float32)
map_col = np.zeros(img.shape, np.float32)

for row in range(row_size):
    for col in range(col_size):
        map_row.itemset((row, col), row)
        map_col.itemset((row, col), col_size - 1 - col)

res = cv.remap(img, map_col, map_row, cv.INTER_LINEAR)
print('img=\n', img)
print('map_row=\n', map_row)
print('map_col=\n', map_col)
print('res=\n', res)

'''
img=
 [[  1  45 239 254 151]
 [196 172 219  82 191]
 [ 47 101 203  24  42]
 [ 72  39 226  50 181]]
map_row=
 [[0. 0. 0. 0. 0.]
 [1. 1. 1. 1. 1.]
 [2. 2. 2. 2. 2.]
 [3. 3. 3. 3. 3.]]
map_col=
 [[4. 3. 2. 1. 0.]
 [4. 3. 2. 1. 0.]
 [4. 3. 2. 1. 0.]
 [4. 3. 2. 1. 0.]]
res=
 [[151 254 239  45   1]
 [191  82 219 172 196]
 [ 42  24 203 101  47]
 [181  50 226  39  72]]
'''
