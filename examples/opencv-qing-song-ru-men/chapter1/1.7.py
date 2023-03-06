# -*- coding: utf-8 -*-
import cv2

lena = cv2.imread("lena.bmp")
r = cv2.imwrite("result.bmp", lena)
