# -*- coding: utf-8 -*-
import cv2 as cv

lena = cv.imread("lena.bmp")
cv.namedWindow("lesson")
cv.imshow("lesson", lena)
cv.waitKey()
