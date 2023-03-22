# -*- coding: utf-8 -*-
import cv2 as cv

a = cv.imread("lena.bmp", cv.IMREAD_GRAYSCALE)
b = a
result1 = a + b
result2 = cv.add(a, b)
cv.imshow("original", a)
cv.imshow("result1", result1)
cv.imshow("result2", result2)
cv.waitKey()
cv.destroyAllWindows()
