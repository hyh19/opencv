# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=(4, 5), dtype=np.uint8)
thresh, res = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)
print(f'img = \n{img}')
print(f'thresh = {thresh}')
print(f'res = \n{res}')

'''
img = 
[[233 189 167  26 144]
 [ 61 231 246  61  25]
 [147 218 229 242  62]
 [185 212 118 136 119]]
thresh = 127.0
res = 
[[  0   0   0  26   0]
 [ 61   0   0  61  25]
 [  0   0   0   0  62]
 [  0   0 118   0 119]]
'''
