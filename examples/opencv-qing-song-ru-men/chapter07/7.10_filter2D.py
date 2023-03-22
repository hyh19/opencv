# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

o = cv.imread("image/lena.bmp")
kernel = np.ones((9, 9), np.float32) / 81
r = cv.filter2D(o, -1, kernel)
cv.imshow("original", o)
cv.imshow("Gaussian", r)
cv.waitKey()
cv.destroyAllWindows()
