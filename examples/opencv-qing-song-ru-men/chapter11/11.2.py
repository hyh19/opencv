# -*- coding: utf-8 -*-
import cv2

o = cv2.imread("lenas.bmp")
r1 = cv2.pyrUp(o)
r2 = cv2.pyrUp(r1)
r3 = cv2.pyrUp(r2)
print("o.shape=", o.shape)
print("r1.shape=", r1.shape)
print("r2.shape=", r2.shape)
print("r3.shape=", r3.shape)
cv2.imshow("original", o)
cv2.imshow("r1", r1)
cv2.imshow("r2", r2)
cv2.imshow("r3", r3)
cv2.waitKey()
cv2.destroyAllWindows()
