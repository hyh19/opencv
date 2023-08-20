# -*- coding: utf-8 -*-
import cv2 as cv

lena = cv.imread("lena.bmp")
cv.imshow("demo1", lena)
cv.imshow("demo2", lena)
cv.waitKey()
cv.destroyAllWindows()
