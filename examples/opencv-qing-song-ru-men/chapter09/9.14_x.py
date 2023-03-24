# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('Laplacian.bmp', cv.IMREAD_GRAYSCALE)
lap = cv.Laplacian(img, cv.CV_64F)
lap = cv.convertScaleAbs(lap)
cv.imshow('img', img)
cv.imshow('lap', lap)
cv.waitKey()
cv.destroyAllWindows()
