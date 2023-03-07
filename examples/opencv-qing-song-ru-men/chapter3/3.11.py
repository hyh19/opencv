# -*- coding: utf-8 -*-
import cv2
import numpy as np

a = cv2.imread("lena.bmp", cv2.IMREAD_COLOR)
w, h, c = a.shape
mask = np.zeros((w, h), dtype=np.uint8)
mask[100:400, 200:400] = 255
mask[100:500, 100:200] = 255
b = cv2.bitwise_and(a, a, mask=mask)
print("a.shape=", a.shape)
print("mask.shape=", mask.shape)
cv2.imshow("a", a)
cv2.imshow("mask", mask)
cv2.imshow("b", b)
cv2.waitKey()
cv2.destroyAllWindows()
