# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

bgr = np.random.randint(0, 256, size=(2, 4, 3), dtype=np.uint8)
gray = cv.cvtColor(bgr, cv.COLOR_BGR2GRAY)
print(f'bgr = \n{bgr}')
print(f'gray = \n{gray}')

'''
bgr = 
[[[247 165  84]
  [ 32 154 140]
  [ 47   7 133]
  [151  24 112]]

 [[253  96 234]
  [145 106 220]
  [ 49 140  25]
  [234 108 207]]]
gray = 
[[150 136  49  65]
 [155 145  95 152]]
'''
