# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=[2, 4], dtype=np.uint8)
rst = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
print("img=\n", img)
print("rst=\n", rst)
