# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://is.gd/CgX82Z

img = cv.imread('lenaNoise.png')
res = cv.blur(img, (5, 5))
cv.imshow('img', img)
cv.imshow('res', res)
cv.waitKey()
cv.destroyAllWindows()
