# -*- coding: utf-8 -*-
import cv2 as cv

lena = cv.imread("lena.bmp")
cv.imshow("demo", lena)
key = cv.waitKey()
if key == ord('a'):
    cv.imshow("PressA", lena)
elif key == ord('b'):
    cv.imshow("PressB", lena)
