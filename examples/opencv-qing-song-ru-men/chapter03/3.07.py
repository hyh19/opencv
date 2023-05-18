# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 255, size=(5, 5), dtype=np.uint8)
mask = np.zeros((5, 5), dtype=np.uint8)
mask[0:3, 0:3] = 255
mask[4, 4] = 255
result = cv.bitwise_and(img, mask)
print(f'img = \n{img}')
print(f'mask = \n{mask}')
print(f'result = \n{result}')

'''
img = 
[[174 124  98  94   0]
 [ 72 122 149  70  22]
 [134 123 177 254 168]
 [248 238 135 242  42]
 [107 245 135 204 231]]
mask = 
[[255 255 255   0   0]
 [255 255 255   0   0]
 [255 255 255   0   0]
 [  0   0   0   0   0]
 [  0   0   0   0 255]]
result = 
[[174 124  98   0   0]
 [ 72 122 149   0   0]
 [134 123 177   0   0]
 [  0   0   0   0   0]
 [  0   0   0   0 231]]
'''
