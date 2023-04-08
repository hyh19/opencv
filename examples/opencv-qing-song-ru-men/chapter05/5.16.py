# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=[4, 5], dtype=np.uint8)
row_size, col_size = img.shape
row_map = np.zeros(img.shape, np.float32)
col_map = np.zeros(img.shape, np.float32)

for row in range(row_size):
    for col in range(col_size):
        row_map.itemset((row, col), row_size - 1 - row)
        col_map.itemset((row, col), col_size - 1 - col)

res = cv.remap(img, col_map, row_map, cv.INTER_LINEAR)
print(f'img = \n{img}')
print(f'row_map = \n{row_map}')
print(f'col_map = \n{col_map}')
print(f'res = \n{res}')

'''
img = 
[[169 133 166 166 203]
 [ 13 239 146 242  28]
 [241  61 132  99 179]
 [ 42 151 252  26   0]]
row_map = 
[[3. 3. 3. 3. 3.]
 [2. 2. 2. 2. 2.]
 [1. 1. 1. 1. 1.]
 [0. 0. 0. 0. 0.]]
col_map = 
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
