# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=[2, 4, 3], dtype=np.uint8)
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
bgr = cv.cvtColor(rgb, cv.COLOR_RGB2BGR)
print("img=\n", img)
print("rgb=\n", rgb)
print("bgr=\n", bgr)
