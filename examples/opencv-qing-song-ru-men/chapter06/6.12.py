# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.zeros((5, 5), dtype=np.uint8)
img[0:6, 0:6] = 123
img[2:6, 2:6] = 126
print(f'img = \n{img}')

thresh1, thresh_img = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
print(f'thresh1 = {thresh1}')
print(f'thresh_img = \n{thresh_img}')

thresh2, otsu_img = cv.threshold(img, 0, 255, cv.THRESH_OTSU)
print(f'thresh2 = {thresh2}')
print(f'otsu_img = \n{otsu_img}')

'''
img = 
[[123 123 123 123 123]
 [123 123 123 123 123]
 [123 123 126 126 126]
 [123 123 126 126 126]
 [123 123 126 126 126]]
thresh1 = 127.0
thresh_img = 
[[0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]]
thresh2 = 123.0
otsu_img = 
[[  0   0   0   0   0]
 [  0   0   0   0   0]
 [  0   0 255 255 255]
 [  0   0 255 255 255]
 [  0   0 255 255 255]]
'''
