# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img1 = np.ones((3, 4), dtype=np.uint8) * 100
img2 = np.ones((3, 4), dtype=np.uint8) * 10
gamma = 3
img3 = cv.addWeighted(img1, 0.6, img2, 5, gamma)
print(f'img1 = \n{img1}')
print(f'img2 = \n{img2}')
print(f'img3 = \n{img3}')

'''
img1 = 
[[100 100 100 100]
 [100 100 100 100]
 [100 100 100 100]]
img2 = 
[[10 10 10 10]
 [10 10 10 10]
 [10 10 10 10]]
img3 = 
[[113 113 113 113]
 [113 113 113 113]
 [113 113 113 113]]
'''
