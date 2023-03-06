# -*- coding: utf-8 -*-
import cv2

lena = cv2.imread("lena.bmp")
cv2.imshow("demo", lena)
key = cv2.waitKey()
if key == ord('a'):
    cv2.imshow("PressA", lena)
elif key == ord('b'):
    cv2.imshow("PressB", lena)
