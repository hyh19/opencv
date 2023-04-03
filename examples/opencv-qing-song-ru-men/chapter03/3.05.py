# -*- coding: utf-8 -*-
import cv2 as cv

a = cv.imread("boat.bmp")
b = cv.imread("lena.bmp")
result = cv.addWeighted(a, 0.6, b, 0.4, 0)
cv.imshow("boat", a)
cv.imshow("lena", b)
cv.imshow("result", result)
cv.waitKey()
cv.destroyAllWindows()
