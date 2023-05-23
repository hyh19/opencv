# -*- coding: utf-8 -*-
import cv2 as cv

img_gray = cv.imread('scharr.bmp', cv.IMREAD_GRAYSCALE)
img_scharr_xy = cv.Scharr(img_gray, cv.CV_64F, 1, 1)
cv.imshow('gray', img_gray)
cv.imshow('scharr_xy', img_scharr_xy)
cv.waitKey()
cv.destroyAllWindows()

'''
error: (-215:Assertion failed) dx >= 0 && dy >= 0 && dx+dy == 1 in function 'getScharrKernels'
'''
