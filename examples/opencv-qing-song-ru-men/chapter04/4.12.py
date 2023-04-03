# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

bgr = np.random.randint(0, 256, size=[2, 3, 3], dtype=np.uint8)
bgr_alpha_255 = cv.cvtColor(bgr, cv.COLOR_BGR2BGRA)
print("bgr=\n", bgr)
print("bgr_alpha_255=\n", bgr_alpha_255)

blue, green, red, alpha = cv.split(bgr_alpha_255)
print("alpha=\n", alpha)

alpha[:, :] = 125
bgr_alpha_125 = cv.merge([blue, green, red, alpha])
print("bgr_alpha_125=\n", bgr_alpha_125)

"""
bgr=
 [[[140 196 129]
  [101 125  71]
  [ 32 159 180]]

 [[212 231  21]
  [250 174  87]
  [187  49  54]]]
bgr_alpha_255=
 [[[140 196 129 255]
  [101 125  71 255]
  [ 32 159 180 255]]

 [[212 231  21 255]
  [250 174  87 255]
  [187  49  54 255]]]
alpha=
 [[255 255 255]
 [255 255 255]]
bgr_alpha_125=
 [[[140 196 129 125]
  [101 125  71 125]
  [ 32 159 180 125]]

 [[212 231  21 125]
  [250 174  87 125]
  [187  49  54 125]]]
"""
