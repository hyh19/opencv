# -*- coding: utf-8 -*-
import numpy as np

img = np.zeros((2, 4, 3), dtype=np.uint8)
print(f'img = \n{img}')
print(f'读取像素点 img[0,3] = {img[0, 3]}')
print(f'读取像素点 img[1,2,2] = {img[1, 2, 2]}')
img[0, 3] = 255
img[0, 0] = [66, 77, 88]
img[1, 1, 1] = 3
img[1, 2, 2] = 4
img[0, 2, 0] = 5
print(f'修改后 img = \n{img}')
print(f'读取修改后像素点 img[1,2,2] = {img[1, 2, 2]}')

'''
img = 
[[[0 0 0]
  [0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]
  [0 0 0]]]
读取像素点 img[0,3] = [0 0 0]
读取像素点 img[1,2,2] = 0
修改后 img = 
[[[ 66  77  88]
  [  0   0   0]
  [  5   0   0]
  [255 255 255]]

 [[  0   0   0]
  [  0   3   0]
  [  0   0   4]
  [  0   0   0]]]
读取修改后像素点 img[1,2,2] = 4
'''