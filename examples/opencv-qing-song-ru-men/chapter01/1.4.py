# -*- coding: utf-8 -*-

import cv2

lena = cv2.imread("lena.bmp")
cv2.imshow("demo", lena)
key = cv2.waitKey()
if key != -1:
    print("触发了按键")
