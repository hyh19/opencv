# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

bgr = np.random.randint(0, 256, size=(2, 4, 3), dtype=np.uint8)
rgb = cv.cvtColor(bgr, cv.COLOR_BGR2RGB)
print(f'bgr = \n{bgr}')
print(f'rgb = \n{rgb}')

'''
bgr = 
[[[214  17 180]
  [169 243  37]
  [ 31  11 107]
  [225 241  67]]

 [[244 206 175]
  [ 31 104  16]
  [144 245 145]
  [124  24 154]]]
rgb = 
[[[180  17 214]
  [ 37 243 169]
  [107  11  31]
  [ 67 241 225]]

 [[175 206 244]
  [ 16 104  31]
  [145 245 144]
  [154  24 124]]]
'''
