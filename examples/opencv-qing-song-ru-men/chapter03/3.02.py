# -*- coding: utf-8 -*-
import numpy as np
import cv2 as cv

img1 = np.random.randint(0, 256, size=(3, 3), dtype=np.uint8)
img2 = np.random.randint(0, 256, size=(3, 3), dtype=np.uint8)
img3 = cv.add(img1, img2)
print(f'img1 = \n{img1}')
print(f'img2 = \n{img2}')
print(f'cv.add(img1,img2) = \n{img3}')

'''
img1 = 
[[187 239  64]
 [105 173  45]
 [157 255   2]]
img2 = 
[[225  98 149]
 [248 188  56]
 [207 133 233]]
cv.add(img1,img2) = 
[[255 255 213]
 [255 255 101]
 [255 255 235]]
'''
