# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.zeros((5, 5), np.uint8)
img[1:4, 1:4] = 1
kernel = np.ones((3, 1), np.uint8)
erode_img = cv.erode(img, kernel)
print(f'img = \n{img}')
print(f'kernel = \n{kernel}')
print(f'erode_img = \n{erode_img}')

'''
img = 
[[0 0 0 0 0]
 [0 1 1 1 0]
 [0 1 1 1 0]
 [0 1 1 1 0]
 [0 0 0 0 0]]
kernel = 
[[1]
 [1]
 [1]]
erode_img = 
[[0 0 0 0 0]
 [0 0 0 0 0]
 [0 1 1 1 0]
 [0 0 0 0 0]
 [0 0 0 0 0]]
'''
