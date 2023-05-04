# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.zeros((8, 8), dtype=np.uint8)
print(f'img = \n{img}')
print(f'读取像素点 img[0,3] = {img[0, 3]}')

img[0, 3] = 255
print(f'修改后 img = \n{img}')
print(f'读取修改后像素点 img[0,3] = {img[0, 3]}')

'''
img = 
[[0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]]
读取像素点 img[0,3] = 0
修改后 img = 
[[  0   0   0 255   0   0   0   0]
 [  0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0]]
读取修改后像素点 img[0,3] = 255
'''
