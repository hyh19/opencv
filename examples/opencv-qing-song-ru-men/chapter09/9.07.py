# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread('lena.bmp', cv.IMREAD_GRAYSCALE)
sobelx = cv.Sobel(o, cv.CV_64F, 1, 0)
sobely = cv.Sobel(o, cv.CV_64F, 0, 1)
sobelx = cv.convertScaleAbs(sobelx)  # 转回uint8
sobely = cv.convertScaleAbs(sobely)
sobelxy = cv.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

sobelxy11 = cv.Sobel(o, cv.CV_64F, 1, 1)
sobelxy11 = cv.convertScaleAbs(sobelxy11)

cv.imshow('original', o)
cv.imshow('xy', sobelxy)
cv.imshow('xy11', sobelxy11)
cv.waitKey()
cv.destroyAllWindows()
