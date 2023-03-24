# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

o = cv.imread("dilation.bmp", cv.IMREAD_UNCHANGED)
kernel = np.ones((9, 9), np.uint8)
dilation = cv.dilate(o, kernel)
cv.imshow("original", o)
cv.imshow("dilation", dilation)
cv.waitKey()
cv.destroyAllWindows()
