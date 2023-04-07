# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.ones((2, 4, 3), dtype=np.uint8)
size = img.shape[:2]
res = cv.resize(img, size)
print(f'img.shape = \n{img.shape}')
print(f'img = \n{img}')
print(f'res.shape = \n{res.shape}')
print(f'res = \n{res}')

'''
img.shape = 
(2, 4, 3)
img = 
[[[1 1 1]
  [1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]
  [1 1 1]]]
res.shape = 
(4, 2, 3)
res = 
[[[1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]]]
'''
