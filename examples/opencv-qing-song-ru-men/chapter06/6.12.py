# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.zeros((5, 5), dtype=np.uint8)
img[0:6, 0:6] = 123
img[2:6, 2:6] = 126
print('img=\n', img)

thresh1, res = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
print('thresh1=', thresh1)
print('res=\n', res)

thresh2, otsu = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
print('thresh2=', thresh2)
print('otsu=\n', otsu)

'''
img=
 [[123 123 123 123 123]
 [123 123 123 123 123]
 [123 123 126 126 126]
 [123 123 126 126 126]
 [123 123 126 126 126]]
thresh1= 127.0
res=
 [[0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]]
thresh2= 123.0
otsu=
 [[  0   0   0   0   0]
 [  0   0   0   0   0]
 [  0   0 255 255 255]
 [  0   0 255 255 255]
 [  0   0 255 255 255]]
'''
