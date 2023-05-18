# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

gray = np.random.randint(0, 256, size=(2, 4), dtype=np.uint8)
bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
print(f'gray = \n{gray}')
print(f'bgr = \n{bgr}')

'''
gray = 
[[146 250  81  82]
 [198 254  15 238]]
bgr = 
[[[146 146 146]
  [250 250 250]
  [ 81  81  81]
  [ 82  82  82]]

 [[198 198 198]
  [254 254 254]
  [ 15  15  15]
  [238 238 238]]]
'''
