# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=[2, 4, 3], dtype=np.uint8)
rst = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print("img=\n", img)
print("rst=\n", rst)
print("像素点(1,0)直接计算得到的值=",
      img[1, 0, 0] * 0.114 + img[1, 0, 1] * 0.587 + img[1, 0, 2] * 0.299)
print("像素点(1,0)使用公式cv2.cvtColor()转换值=", rst[1, 0])
'''
print(img[1,0,0])
print(img[1,0,1])
print(img[1,0,2])
'''
