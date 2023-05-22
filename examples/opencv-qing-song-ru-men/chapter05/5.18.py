# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=(4, 6), dtype=np.uint8)
row_size, col_size = img.shape
map_row = np.zeros(img.shape, np.float32)
map_col = np.zeros(img.shape, np.float32)

for row in range(row_size):
    for col in range(col_size):
        map_row.itemset((row, col), col)
        map_col.itemset((row, col), row)

res = cv.remap(img, map_col, map_row, cv.INTER_LINEAR)
print(f'img = \n{img}')
print(f'map_row = \n{map_row}')
print(f'map_col = \n{map_col}')
print(f'res = \n{res}')

'''
img = 
[[147 246  86 141 253  49]
 [186 176 129 169 184 115]
 [187  14  18 173 176  83]
 [ 63 119 106 246   6 164]]
map_row = 
[[0. 1. 2. 3. 4. 5.]
 [0. 1. 2. 3. 4. 5.]
 [0. 1. 2. 3. 4. 5.]
 [0. 1. 2. 3. 4. 5.]]
map_col = 
[[0. 0. 0. 0. 0. 0.]
 [1. 1. 1. 1. 1. 1.]
 [2. 2. 2. 2. 2. 2.]
 [3. 3. 3. 3. 3. 3.]]
res = 
[[147 186 187  63   0   0]
 [246 176  14 119   0   0]
 [ 86 129  18 106   0   0]
 [141 169 173 246   0   0]]
'''
