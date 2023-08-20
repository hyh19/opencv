# -*- coding: utf-8 -*-

import cv2 as cv

lena = cv.imread("lena.bmp")
cv.imshow("demo", lena)
key = cv.waitKey()
if key != -1:
    print("触发了按键")
