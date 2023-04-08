# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=(4, 5), dtype=np.uint8)
thresh, res = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
print(f'img = \n{img}')
print(f'thresh = {thresh}')
print(f'res = \n{res}')

'''
img = 
[[181  88 190  26  12]
 [ 60  68   4 212 208]
 [221 213 156  83  89]
 [243  92  64 147  20]]
thresh = 127.0
res = 
[[181   0 190   0   0]
 [  0   0   0 212 208]
 [221 213 156   0   0]
 [243   0   0 147   0]]
'''
