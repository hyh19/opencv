# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread('sobel4.bmp', cv.IMREAD_GRAYSCALE)
sobelx = cv.Sobel(o, cv.CV_64F, 1, 0)
sobelx = cv.convertScaleAbs(sobelx)  # 转回uint8
cv.imshow("original", o)
cv.imshow("x", sobelx)
cv.waitKey()
cv.destroyAllWindows()
