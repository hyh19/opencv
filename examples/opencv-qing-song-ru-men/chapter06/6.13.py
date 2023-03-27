# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://is.gd/MtMn52

img = cv.imread('tiffany.bmp', cv.IMREAD_GRAYSCALE)
thresh1, res = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
thresh2, otsu = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
cv.imshow('img', img)
cv.imshow('res', res)
cv.imshow('otus', otsu)
cv.waitKey()
cv.destroyAllWindows()
