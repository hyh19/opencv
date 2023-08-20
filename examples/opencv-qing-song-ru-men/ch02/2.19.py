# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://is.gd/uP3izu

gray = cv.imread('lena.bmp', cv.IMREAD_GRAYSCALE)
cv.imshow('gray', gray)
print('图像gray属性：')
print('gray.shape=', gray.shape)
print('gray.size=', gray.size)
print('gray.dtype=', gray.dtype)

color = cv.imread('lenacolor.png')
cv.imshow('color', color)
print('图像color属性：')
print('color.shape=', color.shape)
print('color.size=', color.size)
print('color.dtype=', color.dtype)

cv.waitKey()
cv.destroyAllWindows()

'''
图像gray属性：
gray.shape= (256, 256)
gray.size= 65536
gray.dtype= uint8
图像color属性：
color.shape= (512, 512, 3)
color.size= 786432
color.dtype= uint8
'''
