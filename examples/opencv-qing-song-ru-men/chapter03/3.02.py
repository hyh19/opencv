# -*- coding: utf-8 -*-
import numpy as np
import cv2 as cv

img1 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
img2 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
img3 = cv.add(img1, img2)
print("img1=\n", img1)
print("img2=\n", img2)
print("cv.add(img1,img2)=\n", img3)
