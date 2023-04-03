# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

bgr = np.random.randint(0, 256, size=[2, 4, 3], dtype=np.uint8)
gray = cv.cvtColor(bgr, cv.COLOR_BGR2GRAY)
print('bgr=\n', bgr)
print('gray=\n', gray)
print('像素点(1,0)直接计算得到的值=',
      bgr[1, 0, 0] * 0.114 + bgr[1, 0, 1] * 0.587 + bgr[1, 0, 2] * 0.299)
print('像素点(1,0)使用公式cv2.cvtColor()转换值=', gray[1, 0])

'''
bgr=
 [[[123 208 102]
  [152  95  17]
  [213 238 166]
  [140  46 159]]

 [[194 182  76]
  [117 203  81]
  [104  49 199]
  [168 164 233]]]
gray=
 [[167  78 214  91]
 [152 157 100 185]]
像素点(1,0)直接计算得到的值= 151.67399999999998
像素点(1,0)使用公式cv2.cvtColor()转换值= 152
'''
