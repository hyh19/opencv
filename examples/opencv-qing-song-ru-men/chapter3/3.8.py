# -*- coding: utf-8 -*-
import cv2
import numpy as np

a = cv2.imread("lena.bmp", cv2.IMREAD_GRAYSCALE)
b = np.zeros(a.shape, dtype=np.uint8)
b[100:400, 200:400] = 255
b[100:500, 100:200] = 255
c = cv2.bitwise_and(a, b)
cv2.imshow("a", a)
cv2.imshow("b", b)
cv2.imshow("c", c)
cv2.waitKey()
cv2.destroyAllWindows()
