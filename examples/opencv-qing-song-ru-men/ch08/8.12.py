# -*- coding: utf-8 -*-
import cv2 as cv

rect = cv.getStructuringElement(shape=cv.MORPH_RECT, ksize=(5, 5))
cross = cv.getStructuringElement(shape=cv.MORPH_CROSS, ksize=(5, 5))
ellipse = cv.getStructuringElement(shape=cv.MORPH_ELLIPSE, ksize=(5, 5))
print(f'rect = \n{rect}')
print(f'cross = \n{cross}')
print(f'ellipse = \n{ellipse}')

"""
rect = 
[[1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]]
cross = 
[[0 0 1 0 0]
 [0 0 1 0 0]
 [1 1 1 1 1]
 [0 0 1 0 0]
 [0 0 1 0 0]]
ellipse = 
[[0 0 1 0 0]
 [1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]
 [0 0 1 0 0]]
"""
