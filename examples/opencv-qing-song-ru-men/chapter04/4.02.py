# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

gray = np.random.randint(0, 256, size=[2, 4], dtype=np.uint8)
bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
print("gray=\n", gray)
print("bgr=\n", bgr)

"""
gray=
 [[109 116 247  61]
 [178  96 164 105]]
bgr=
 [[[109 109 109]
  [116 116 116]
  [247 247 247]
  [ 61  61  61]]

 [[178 178 178]
  [ 96  96  96]
  [164 164 164]
  [105 105 105]]]
"""
