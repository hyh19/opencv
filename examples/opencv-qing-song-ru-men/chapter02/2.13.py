# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('lenacolor.png')
face = img[220:400, 250:350]
cv.imshow('img', img)
cv.imshow('face', face)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/HHCjND
