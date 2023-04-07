# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread('test.bmp')
res = cv.resize(img, None, fx=2, fy=0.5)
print(f'img.shape = {img.shape}')
print(f'res.shape = {res.shape}')
cv.imshow('img', img)
cv.imshow('res', res)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/LLRYqz

'''
img.shape = (512, 51, 3)
res.shape = (256, 102, 3)
'''
