# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=(4, 5), dtype=np.uint8)
thresh, res = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
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
