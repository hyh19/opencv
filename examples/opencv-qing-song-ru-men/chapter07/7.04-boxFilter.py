# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://is.gd/i9JzkG

img = cv.imread('lenaNoise.png')
res = cv.boxFilter(img, -1, (5, 5), normalize=0)
cv.imshow('img', img)
cv.imshow('res', res)
cv.waitKey()
cv.destroyAllWindows()
