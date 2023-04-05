# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://is.gd/HuDPRy

img = cv.imread('lenaNoise.png')
res = cv.GaussianBlur(img, (5, 5), 0, 0)
cv.imshow('img', img)
cv.imshow('res', res)
cv.waitKey()
cv.destroyAllWindows()
