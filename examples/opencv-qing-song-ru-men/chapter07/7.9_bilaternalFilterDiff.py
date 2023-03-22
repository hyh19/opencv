# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread("image/bilTest.bmp")
g = r = cv.GaussianBlur(o, (55, 55), 0, 0)
b = cv.bilateralFilter(o, 55, 100, 100)
cv.imshow("original", o)
cv.imshow("Gaussian", g)
cv.imshow("bilateral", b)
cv.waitKey()
cv.destroyAllWindows()
