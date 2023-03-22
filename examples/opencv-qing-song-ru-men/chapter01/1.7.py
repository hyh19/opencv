# -*- coding: utf-8 -*-
import cv2 as cv

lena = cv.imread("lena.bmp")
r = cv.imwrite("result.bmp", lena)
