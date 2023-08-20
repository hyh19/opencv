# -*- coding: utf-8 -*-
import numpy as np

img1 = np.random.randint(0, 256, size=(3, 3), dtype=np.uint8)
img2 = np.random.randint(0, 256, size=(3, 3), dtype=np.uint8)
print(f'img1 = \n{img1}')
print(f'img2 = \n{img2}')
print(f'img1 + img2 = \n{img1 + img2}')

'''
img1 = 
[[150 137 250]
 [239 158 135]
 [227 152 176]]
img2 = 
[[176  18  33]
 [ 44  86 208]
 [ 32 130  21]]
img1 + img2 = 
[[ 70 155  27]
 [ 27 244  87]
 [  3  26 197]]
'''
