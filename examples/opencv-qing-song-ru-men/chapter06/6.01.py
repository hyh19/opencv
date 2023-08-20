# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(low=0, high=256, size=(4, 5), dtype=np.uint8)
thresh, res = cv.threshold(img, thresh=127, maxval=255, type=cv.THRESH_BINARY)
print(f'img = \n{img}')
print(f'thresh = {thresh}')
print(f'res = \n{res}')

'''
img = 
[[158  99 134 244 194]
 [ 42 127 124 147 131]
 [251  85 134  39 181]
 [255 191  18  91 145]]
thresh = 127.0
res = 
[[255   0 255 255 255]
 [  0   0   0 255 255]
 [255   0 255   0 255]
 [255 255   0   0 255]]
'''
