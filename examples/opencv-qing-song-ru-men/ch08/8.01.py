# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.zeros(shape=(5, 5), dtype=np.uint8)
img[1:4, 1:4] = 1
kernel = np.ones(shape=(3, 1), dtype=np.uint8)
img_erode = cv.erode(img, kernel)
print(f'img = \n{img}')
print(f'kernel = \n{kernel}')
print(f'img_erode = \n{img_erode}')

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
img_erode = 
[[0 0 0 0 0]
 [0 0 0 0 0]
 [0 1 1 1 0]
 [0 0 0 0 0]
 [0 0 0 0 0]]
'''
