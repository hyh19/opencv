# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = np.ones([2, 4, 3], dtype=np.uint8)
size = img.shape[:2]
rst = cv2.resize(img, size)
print("img.shape=\n", img.shape)
print("img=\n", img)
print("rst.shape=\n", rst.shape)
print("rst=\n", rst)
