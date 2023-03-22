# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread('sobel4.bmp', cv.IMREAD_GRAYSCALE)
sobely = cv.Sobel(o, cv.CV_64F, 0, 1)
sobely = cv.convertScaleAbs(sobely)
cv.imshow("original", o)
cv.imshow("y", sobely)
cv.waitKey()
cv.destroyAllWindows()
