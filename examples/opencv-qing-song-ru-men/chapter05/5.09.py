# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=[4, 5], dtype=np.uint8)
rows, cols = img.shape
map_row = np.zeros(img.shape, np.float32)
map_col = np.ones(img.shape, np.float32) * 3
res = cv.remap(img, map_col, map_row, cv.INTER_LINEAR)
print('img=\n', img)
print('map_row=\n', map_row)
print('map_col=\n', map_col)
print('res=\n', res)

'''
img=
 [[ 37 191 172  16  23]
 [176 232 191  71 127]
 [136 147 194  51  50]
 [109  36   0 139 131]]
map_row=
 [[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]
map_col=
 [[3. 3. 3. 3. 3.]
 [3. 3. 3. 3. 3.]
 [3. 3. 3. 3. 3.]
 [3. 3. 3. 3. 3.]]
res=
 [[16 16 16 16 16]
 [16 16 16 16 16]
 [16 16 16 16 16]
 [16 16 16 16 16]]
'''
