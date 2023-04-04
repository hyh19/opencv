# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=[4, 6], dtype=np.uint8)
row_size, col_size = img.shape
map_row = np.zeros(img.shape, np.float32)
map_col = np.zeros(img.shape, np.float32)

for row in range(row_size):
    for col in range(col_size):
        map_row.itemset((row, col), col)
        map_col.itemset((row, col), row)

res = cv.remap(img, map_col, map_row, cv.INTER_LINEAR)
print('img=\n', img)
print('map_row=\n', map_row)
print('map_col=\n', map_col)
print('res=\n', res)

'''
img=
 [[229 148   7 231 250 169]
 [140 135 169 190 215 157]
 [ 64  48 177 107 193  61]
 [170 249 241 178   5  89]]
map_row=
 [[0. 1. 2. 3. 4. 5.]
 [0. 1. 2. 3. 4. 5.]
 [0. 1. 2. 3. 4. 5.]
 [0. 1. 2. 3. 4. 5.]]
map_col=
 [[0. 0. 0. 0. 0. 0.]
 [1. 1. 1. 1. 1. 1.]
 [2. 2. 2. 2. 2. 2.]
 [3. 3. 3. 3. 3. 3.]]
res=
 [[229 140  64 170   0   0]
 [148 135  48 249   0   0]
 [  7 169 177 241   0   0]
 [231 190 107 178   0   0]]
'''
