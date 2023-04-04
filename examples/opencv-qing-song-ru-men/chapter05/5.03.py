# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('test.bmp')
res = cv.resize(img, None, fx=2, fy=0.5)
print('img.shape=', img.shape)
print('res.shape=', res.shape)

'''
img.shape= (512, 51, 3)
res.shape= (256, 102, 3)
'''
