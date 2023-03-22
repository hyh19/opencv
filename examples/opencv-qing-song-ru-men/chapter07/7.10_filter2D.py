# -*- coding: utf-8 -*-
import cv2
import numpy as np

o = cv2.imread("image/lena.bmp")
kernel = np.ones((9, 9), np.float32) / 81
r = cv2.filter2D(o, -1, kernel)
cv2.imshow("original", o)
cv2.imshow("Gaussian", r)
cv2.waitKey()
cv2.destroyAllWindows()
