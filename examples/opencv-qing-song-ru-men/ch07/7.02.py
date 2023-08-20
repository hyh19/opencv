# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('lenaNoise.png')
res5 = cv.blur(img, ksize=(5, 5))
res30 = cv.blur(img, ksize=(30, 30))
cv.imshow('img', img)
cv.imshow('res5', res5)
cv.imshow('res30', res30)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/NUFTTg
