# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('lenaNoise.png')
res = cv.blur(img, ksize=(5, 5))
cv.imshow('img', img)
cv.imshow('res', res)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/CgX82Z
