# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread("lena.bmp")
G0 = o
G1 = cv.pyrDown(G0)
G2 = cv.pyrDown(G1)
G3 = cv.pyrDown(G2)
L0 = G0 - cv.pyrUp(G1)
L1 = G1 - cv.pyrUp(G2)
L2 = G2 - cv.pyrUp(G3)
print("L0.shape=", L0.shape)
print("L1.shape=", L1.shape)
print("L2.shape=", L2.shape)
cv.imshow("L0", L0)
cv.imshow("L1", L1)
cv.imshow("L2", L2)
cv.waitKey()
cv.destroyAllWindows()
