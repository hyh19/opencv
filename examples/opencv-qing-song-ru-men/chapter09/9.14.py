# -*- coding: utf-8 -*-
import cv2 as cv

gray_img = cv.imread('Laplacian.bmp', cv.IMREAD_GRAYSCALE)
laplacian_img = cv.Laplacian(gray_img, cv.CV_64F)
laplacian_img = cv.convertScaleAbs(laplacian_img)
cv.imshow('gray', gray_img)
cv.imshow('laplacian', laplacian_img)
cv.waitKey()
cv.destroyAllWindows()
