# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread('Laplacian.bmp', cv.IMREAD_GRAYSCALE)
Laplacian = cv.Laplacian(o, cv.CV_64F)
Laplacian = cv.convertScaleAbs(Laplacian)
cv.imshow('original', o)
cv.imshow('Laplacian', Laplacian)
cv.waitKey()
cv.destroyAllWindows()
