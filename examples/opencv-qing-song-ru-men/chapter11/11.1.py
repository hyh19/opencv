# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread("lena.bmp", cv.IMREAD_GRAYSCALE)
r1 = cv.pyrDown(o)
r2 = cv.pyrDown(r1)
r3 = cv.pyrDown(r2)
print("o.shape=", o.shape)
print("r1.shape=", r1.shape)
print("r2.shape=", r2.shape)
print("r3.shape=", r3.shape)
cv.imshow("original", o)
cv.imshow("r1", r1)
cv.imshow("r2", r2)
cv.imshow("r3", r3)
cv.waitKey()
cv.destroyAllWindows()
