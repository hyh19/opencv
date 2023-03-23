# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img1 = cv.imread("opening.bmp")
img2 = cv.imread("opening2.bmp")
k = np.ones((10, 10), np.uint8)
r1 = cv.morphologyEx(img1, cv.MORPH_OPEN, k)
r2 = cv.morphologyEx(img2, cv.MORPH_OPEN, k)
cv.imshow("img1", img1)
cv.imshow("result1", r1)
cv.imshow("img2", img2)
cv.imshow("result2", r2)
cv.waitKey()
cv.destroyAllWindows()