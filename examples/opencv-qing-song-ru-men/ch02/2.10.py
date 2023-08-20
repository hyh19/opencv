# -*- coding: utf-8 -*-
import numpy as np

img = np.random.randint(10, 99, size=(2, 4, 3), dtype=np.uint8)
print(f'img = \n{img}')
print(f'读取像素点 img[1,2,0] = {img.item(1, 2, 0)}')
print(f'读取像素点 img[0,2,1] = {img.item(0, 2, 1)}')
print(f'读取像素点 img[1,0,2] = {img.item(1, 0, 2)}')
img.itemset((1, 2, 0), 255)
img.itemset((0, 2, 1), 255)
img.itemset((1, 0, 2), 255)
print(f'修改后 img = \n{img}')
print(f'修改后像素点 img[1,2,0] = {img.item(1, 2, 0)}')
print(f'修改后像素点 img[0,2,1] = {img.item(0, 2, 1)}')
print(f'修改后像素点 img[1,0,2] = {img.item(1, 0, 2)}')

'''
img = 
[[[87 82 25]
  [87 64 20]
  [36 48 72]
  [48 52 32]]

 [[93 20 77]
  [29 75 97]
  [81 88 89]
  [51 31 59]]]
读取像素点 img[1,2,0] = 81
读取像素点 img[0,2,1] = 48
读取像素点 img[1,0,2] = 77
修改后 img = 
[[[ 87  82  25]
  [ 87  64  20]
  [ 36 255  72]
  [ 48  52  32]]

 [[ 93  20 255]
  [ 29  75  97]
  [255  88  89]
  [ 51  31  59]]]
修改后像素点 img[1,2,0] = 255
修改后像素点 img[0,2,1] = 255
修改后像素点 img[1,0,2] = 255
'''
