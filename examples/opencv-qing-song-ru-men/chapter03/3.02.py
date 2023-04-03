# -*- coding: utf-8 -*-
import numpy as np
import cv2 as cv

img1 = np.random.randint(0, 256, size=(3, 3), dtype=np.uint8)
img2 = np.random.randint(0, 256, size=(3, 3), dtype=np.uint8)
img3 = cv.add(img1, img2)
print('img1=\n', img1)
print('img2=\n', img2)
print('cv.add(img1,img2)=\n', img3)

'''
img1=
 [[ 27 247  83]
 [221 124 157]
 [100 160 241]]
img2=
 [[204 248 226]
 [196 166 104]
 [ 31  75 203]]
cv.add(img1,img2)=
 [[231 255 255]
 [255 255 255]
 [131 235 255]]
'''
