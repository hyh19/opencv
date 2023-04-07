# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=(4, 5), dtype=np.uint8)
row_map = np.zeros(img.shape, np.float32)
col_map = np.ones(img.shape, np.float32) * 3
res = cv.remap(img, col_map, row_map, cv.INTER_LINEAR)
print(f'img = \n{img}')
print(f'row_map = \n{row_map}')
print(f'col_map = \n{col_map}')
print(f'res = \n{res}')

'''
img = 
[[ 68 110  83 202 183]
 [ 96 224  46  70 214]
 [167  58 165  72 141]
 [ 37 168  95 144 168]]
row_map = 
[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]
col_map = 
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
