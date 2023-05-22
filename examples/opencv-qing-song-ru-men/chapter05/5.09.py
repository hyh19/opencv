# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=(4, 5), dtype=np.uint8)
map_row = np.zeros(img.shape, np.float32)
map_col = np.ones(img.shape, np.float32) * 3
res = cv.remap(img, map_col, map_row, cv.INTER_LINEAR)
print(f'img = \n{img}')
print(f'map_row = \n{map_row}')
print(f'map_col = \n{map_col}')
print(f'res = \n{res}')

'''
img = 
[[ 68 110  83 202 183]
 [ 96 224  46  70 214]
 [167  58 165  72 141]
 [ 37 168  95 144 168]]
map_row = 
[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]
map_col = 
[[3. 3. 3. 3. 3.]
 [3. 3. 3. 3. 3.]
 [3. 3. 3. 3. 3.]
 [3. 3. 3. 3. 3.]]
res = 
[[202 202 202 202 202]
 [202 202 202 202 202]
 [202 202 202 202 202]
 [202 202 202 202 202]]
'''
