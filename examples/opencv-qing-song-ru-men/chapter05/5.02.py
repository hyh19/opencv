# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://is.gd/twtfOh

img = cv.imread('test.bmp')
rows, cols = img.shape[:2]
size = (int(cols * 0.9), int(rows * 0.5))
res = cv.resize(img, size)
print('img.shape=', img.shape)
print('res.shape=', res.shape)
cv.imshow('img', img)
cv.imshow('res', res)
cv.waitKey()
cv.destroyAllWindows()

'''
img.shape= (512, 51, 3)
res.shape= (256, 45, 3)
'''
