# -*- coding: utf-8 -*-
import cv2 as cv

img_gray = cv.imread('Laplacian.bmp', cv.IMREAD_GRAYSCALE)
laplacian = cv.Laplacian(img_gray, cv.CV_64F)
laplacian = cv.convertScaleAbs(laplacian)
cv.imshow('img_gray', img_gray)
cv.imshow('laplacian', laplacian)
cv.waitKey()
cv.destroyAllWindows()
