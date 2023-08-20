# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(low=0, high=256, size=(4, 5), dtype=np.uint8)
thresh, res = cv.threshold(img, thresh=127, maxval=255, type=cv.THRESH_TRUNC)
print(f'img = \n{img}')
print(f'thresh = {thresh}')
print(f'res = \n{res}')

'''
img = 
[[247   8  47 136 213]
 [134 206 233  28 233]
 [ 92  56  10 118  31]
 [236 127 139  49 179]]
thresh = 127.0
res = 
[[127   8  47 127 127]
 [127 127 127  28 127]
 [ 92  56  10 118  31]
 [127 127 127  49 127]]
'''
