# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

bgr_img = np.random.randint(0, 256, size=(2, 3, 3), dtype=np.uint8)
bgra_img = cv.cvtColor(bgr_img, cv.COLOR_BGR2BGRA)
print(f'bgr = \n{bgr_img}')
print(f'bgra = \n{bgra_img}')

'''
bgr = 
[[[176 207 171]
  [ 41  32 193]
  [209 135 155]]

 [[166  79 196]
  [120 155 176]
  [ 42 209 112]]]
bgra = 
[[[176 207 171 255]
  [ 41  32 193 255]
  [209 135 155 255]]

 [[166  79 196 255]
  [120 155 176 255]
  [ 42 209 112 255]]]
'''
