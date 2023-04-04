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
        map_col.itemset((row, col), col_size - 1 - col)

res = cv.remap(img, map_col, map_row, cv.INTER_LINEAR)
print('img=\n', img)
print('map_row=\n', map_row)
print('map_col=\n', map_col)
print('res=\n', res)

'''
img=
 [[ 93  25 151 106  32]
 [127 182  43 102  53]
 [121 102  30   4 130]
 [178 183 171 243  71]]
map_row=
 [[3. 3. 3. 3. 3.]
 [2. 2. 2. 2. 2.]
 [1. 1. 1. 1. 1.]
 [0. 0. 0. 0. 0.]]
map_col=
 [[4. 3. 2. 1. 0.]
 [4. 3. 2. 1. 0.]
 [4. 3. 2. 1. 0.]
 [4. 3. 2. 1. 0.]]
res=
 [[ 71 243 171 183 178]
 [130   4  30 102 121]
 [ 53 102  43 182 127]
 [ 32 106 151  25  93]]
'''
