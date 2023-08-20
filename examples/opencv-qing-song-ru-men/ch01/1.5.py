# -*- coding: utf-8 -*-
import cv2 as cv

lena = cv.imread("lenacolor.png")
cv.imshow("demo", lena)
cv.waitKey()
cv.destroyWindow("demo")
