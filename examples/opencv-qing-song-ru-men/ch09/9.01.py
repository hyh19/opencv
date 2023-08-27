# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

a = np.random.randint(low=-256, high=256, size=(4, 5), dtype=np.int16)
res = cv.convertScaleAbs(a)
print(f'a = \n{a}')
print(f'res = \n{res}')

'''
a = 
[[  93  167  240  -21   63]
 [  50 -140  166  -18  152]
 [ -76  171  -63  158  203]
 [ -59   32  -29   39 -151]]
res = 
[[ 93 167 240  21  63]
 [ 50 140 166  18 152]
 [ 76 171  63 158 203]
 [ 59  32  29  39 151]]
'''
