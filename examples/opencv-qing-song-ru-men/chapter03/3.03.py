# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://is.gd/3kOFmH

gray = cv.imread('lena.bmp', cv.IMREAD_GRAYSCALE)
result1 = gray + gray
result2 = cv.add(gray, gray)
cv.imshow('gray', gray)
cv.imshow('result1', result1)
cv.imshow('result2', result2)
cv.waitKey()
cv.destroyAllWindows()
