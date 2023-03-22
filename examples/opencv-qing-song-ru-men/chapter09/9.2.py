# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread('sobel4.bmp', cv.IMREAD_GRAYSCALE)
sobelx = cv.Sobel(o, -1, 1, 0)
cv.imshow("original", o)
cv.imshow("x", sobelx)
cv.waitKey()
cv.destroyAllWindows()
