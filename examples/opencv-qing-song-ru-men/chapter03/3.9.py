# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

a = cv.imread("lena.bmp", cv.IMREAD_COLOR)
b = np.zeros(a.shape, dtype=np.uint8)
b[100:400, 200:400] = 255
b[100:500, 100:200] = 255
c = cv.bitwise_and(a, b)
print("a.shape=", a.shape)
print("b.shape=", b.shape)
cv.imshow("a", a)
cv.imshow("b", b)
cv.imshow("c", c)
cv.waitKey()
cv.destroyAllWindows()
