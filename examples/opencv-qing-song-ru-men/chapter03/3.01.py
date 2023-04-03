# -*- coding: utf-8 -*-
import numpy as np

img1 = np.random.randint(0, 256, size=(3, 3), dtype=np.uint8)
img2 = np.random.randint(0, 256, size=(3, 3), dtype=np.uint8)
print('img1=\n', img1)
print('img2=\n', img2)
print('img1+img2=\n', img1 + img2)

'''
img1=
 [[246  30  26]
 [ 87  37 246]
 [  5  25  64]]
img2=
 [[211 114  13]
 [169  95 249]
 [104   6 214]]
img1+img2=
 [[201 144  39]
 [  0 132 239]
 [109  31  22]]
'''
