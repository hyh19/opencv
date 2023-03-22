# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread("lena.bmp", cv.IMREAD_GRAYSCALE)
r1 = cv.Canny(o, 128, 200)
r2 = cv.Canny(o, 32, 128)
cv.imshow("original", o)
cv.imshow("result1", r1)
cv.imshow("result2", r2)
cv.waitKey()
cv.destroyAllWindows()
