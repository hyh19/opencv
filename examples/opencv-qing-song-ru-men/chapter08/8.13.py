# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread("kernel.bmp", cv.IMREAD_UNCHANGED)
kernel1 = cv.getStructuringElement(cv.MORPH_RECT, (59, 59))
kernel2 = cv.getStructuringElement(cv.MORPH_CROSS, (59, 59))
kernel3 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (59, 59))
dst1 = cv.dilate(o, kernel1)
dst2 = cv.dilate(o, kernel2)
dst3 = cv.dilate(o, kernel3)
cv.imshow("original", o)
cv.imshow("dst1", dst1)
cv.imshow("dst2", dst2)
cv.imshow("dst3", dst3)
cv.waitKey()
cv.destroyAllWindows()
