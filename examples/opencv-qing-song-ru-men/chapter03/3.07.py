# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

a = np.random.randint(0, 255, (5, 5), dtype=np.uint8)
b = np.zeros((5, 5), dtype=np.uint8)
b[0:3, 0:3] = 255
b[4, 4] = 255
c = cv.bitwise_and(a, b)
print('a=\n', a)
print('b=\n', b)
print('c=\n', c)

'''
a=
 [[ 22  46  92  21  83]
 [ 11 160 241 150 234]
 [ 28  51  41 162  17]
 [184 224  59 140 186]
 [200 204 168 106 115]]
b=
 [[255 255 255   0   0]
 [255 255 255   0   0]
 [255 255 255   0   0]
 [  0   0   0   0   0]
 [  0   0   0   0 255]]
c=
 [[ 22  46  92   0   0]
 [ 11 160 241   0   0]
 [ 28  51  41   0   0]
 [  0   0   0   0   0]
 [  0   0   0   0 115]]
'''
