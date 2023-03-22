# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread('sobel4.bmp', cv.IMREAD_GRAYSCALE)
sobelxy = cv.Sobel(o, cv.CV_64F, 1, 1)
sobelxy = cv.convertScaleAbs(sobelxy)
cv.imshow("original", o)
cv.imshow("xy", sobelxy)
cv.waitKey()
cv.destroyAllWindows()
