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

"""
img1=
 [[3 3 3 3]
 [3 3 3 3]
 [3 3 3 3]
 [3 3 3 3]]
img2=
 [[5 5 5 5]
 [5 5 5 5]
 [5 5 5 5]
 [5 5 5 5]]
cv.add(img1,img2)=
 [[8 8 8 8]
 [8 8 8 8]
 [8 8 8 8]
 [8 8 8 8]]
cv.add(img1,6)
 [[9 9 9 9]
 [9 9 9 9]
 [9 9 9 9]
 [9 9 9 9]]
cv.add(6,img2)=
 [[11 11 11 11]
 [11 11 11 11]
 [11 11 11 11]
 [11 11 11 11]]
"""
