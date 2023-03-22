# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

a = cv.imread("lena.bmp", cv.IMREAD_COLOR)
w, h, c = a.shape
mask = np.zeros((w, h), dtype=np.uint8)
mask[100:400, 200:400] = 255
mask[100:500, 100:200] = 255
b = cv.bitwise_and(a, a, mask=mask)
print("a.shape=", a.shape)
print("mask.shape=", mask.shape)
cv.imshow("a", a)
cv.imshow("mask", mask)
cv.imshow("b", b)
cv.waitKey()
cv.destroyAllWindows()
