# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('Laplacian.bmp', cv.IMREAD_GRAYSCALE)
laplacian = cv.Laplacian(img, cv.CV_64F)
laplacian = cv.convertScaleAbs(laplacian)
cv.imshow('img', img)
cv.imshow('laplacian', laplacian)
cv.waitKey()
cv.destroyAllWindows()
