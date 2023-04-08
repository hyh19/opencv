# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=(4, 5), dtype=np.uint8)
row_size, col_size = img.shape
row_map = np.zeros(img.shape, np.float32)
col_map = np.zeros(img.shape, np.float32)

for row in range(row_size):
    for col in range(col_size):
        row_map.itemset((row, col), row)
        col_map.itemset((row, col), col_size - 1 - col)

res = cv.remap(img, col_map, row_map, cv.INTER_LINEAR)
print(f'img = \n{img}')
print(f'row_map = \n{row_map}')
print(f'col_map = \n{col_map}')
print(f'res = \n{res}')

'''
img = 
[[122  74 150 204 195]
 [126 149 191  32 140]
 [100 105  69 223 112]
 [ 29 235 165 247 224]]
row_map = 
[[0. 0. 0. 0. 0.]
 [1. 1. 1. 1. 1.]
 [2. 2. 2. 2. 2.]
 [3. 3. 3. 3. 3.]]
col_map = 
[[4. 3. 2. 1. 0.]
 [4. 3. 2. 1. 0.]
 [4. 3. 2. 1. 0.]
 [4. 3. 2. 1. 0.]]
res = 
[[195 204 150  74 122]
 [140  32 191 149 126]
 [112 223  69 105 100]
 [224 247 165 235  29]]
'''
