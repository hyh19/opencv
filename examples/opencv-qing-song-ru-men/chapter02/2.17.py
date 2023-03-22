# -*- coding: utf-8 -*-
import cv2 as cv

lena = cv.imread("lenacolor.png")
b, g, r = cv.split(lena)
cv.imshow("B", b)
cv.imshow("G", g)
cv.imshow("R", r)
cv.waitKey()
cv.destroyAllWindows()
