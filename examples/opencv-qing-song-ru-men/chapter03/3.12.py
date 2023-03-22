# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img1 = np.ones((4, 4), dtype=np.uint8) * 3
img2 = np.ones((4, 4), dtype=np.uint8) * 5
print("img1=\n", img1)
print("img2=\n", img2)
img3 = cv.add(img1, img2)
print("cv.add(img1,img2)=\n", img3)
img4 = cv.add(img1, 6)
print("cv.add(img1,6)\n", img4)
img5 = cv.add(6, img2)
print("cv.add(6,img2)=\n", img5)
