# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread('scharr.bmp', cv.IMREAD_GRAYSCALE)
scharrxy11 = cv.Scharr(o, cv.CV_64F, 1, 1)
cv.imshow("original", o)
cv.imshow("xy11", scharrxy11)
cv.waitKey()
cv.destroyAllWindows()
