# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=(4, 5), dtype=np.uint8)
row_size, col_size = img.shape
map_row = np.zeros(img.shape, np.float32)
map_col = np.zeros(img.shape, np.float32)

for row in range(row_size):
    for col in range(col_size):
        map_row.itemset((row, col), row_size - 1 - row)
        map_col.itemset((row, col), col_size - 1 - col)

res = cv.remap(img, map_col, map_row, cv.INTER_LINEAR)
print(f'img = \n{img}')
print(f'map_row = \n{map_row}')
print(f'map_col = \n{map_col}')
print(f'res = \n{res}')

'''
img = 
[[169 133 166 166 203]
 [ 13 239 146 242  28]
 [241  61 132  99 179]
 [ 42 151 252  26   0]]
map_row = 
[[3. 3. 3. 3. 3.]
 [2. 2. 2. 2. 2.]
 [1. 1. 1. 1. 1.]
 [0. 0. 0. 0. 0.]]
map_col = 
[[4. 3. 2. 1. 0.]
 [4. 3. 2. 1. 0.]
 [4. 3. 2. 1. 0.]
 [4. 3. 2. 1. 0.]]
res = 
[[  0  26 252 151  42]
 [179  99 132  61 241]
 [ 28 242 146 239  13]
 [203 166 166 133 169]]
'''
