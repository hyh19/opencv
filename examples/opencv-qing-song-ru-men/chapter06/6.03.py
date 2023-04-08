# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=(4, 5), dtype=np.uint8)
thresh, res = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
print(f'img = \n{img}')
print(f'thresh = {thresh}')
print(f'res = \n{res}')

'''
img = 
[[180 237 160  61 107]
 [101 200  68  60 100]
 [158 166 103  65 118]
 [ 15 121  42  92 120]]
thresh = 127.0
res = 
[[  0   0   0 255 255]
 [255   0 255 255 255]
 [  0   0 255 255 255]
 [255 255 255 255 255]]
'''
