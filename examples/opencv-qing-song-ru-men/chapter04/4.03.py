# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

bgr = np.random.randint(0, 256, size=(2, 4, 3), dtype=np.uint8)
rgb = cv.cvtColor(bgr, cv.COLOR_BGR2RGB)
bgr1 = cv.cvtColor(rgb, cv.COLOR_RGB2BGR)
print('bgr=\n', bgr)
print('rgb=\n', rgb)
print('bgr1=\n', bgr1)

'''
bgr=
 [[[214 108  40]
  [ 86 125 226]
  [  7 240   1]
  [138 160 108]]

 [[ 87 106  94]
  [117 166 232]
  [220  99 120]
  [238  28 121]]]
rgb=
 [[[ 40 108 214]
  [226 125  86]
  [  1 240   7]
  [108 160 138]]

 [[ 94 106  87]
  [232 166 117]
  [120  99 220]
  [121  28 238]]]
bgr1=
 [[[214 108  40]
  [ 86 125 226]
  [  7 240   1]
  [138 160 108]]

 [[ 87 106  94]
  [117 166 232]
  [220  99 120]
  [238  28 121]]]
'''
