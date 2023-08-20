# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=(5, 5), dtype=np.uint8)
mask = cv.inRange(img, 100, 200)
print(f'img = \n{img}')
print(f'mask = \n{mask}')

'''
img = 
[[ 49 141  87  39  66]
 [ 14 188 202  46 219]
 [195  87  62  49  83]
 [249 101  48 195 110]
 [ 95 157 250 159 237]]
mask = 
[[  0 255   0   0   0]
 [  0 255   0   0   0]
 [255   0   0   0   0]
 [  0 255   0 255 255]
 [  0 255   0 255   0]]
'''
