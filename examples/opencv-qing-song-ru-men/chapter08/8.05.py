# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread('dilation.bmp')
kernel = np.ones((9, 9), np.uint8)
dilate_img = cv.dilate(img, kernel)
cv.imshow('img', img)
cv.imshow('dilate', dilate_img)
cv.waitKey()
cv.destroyAllWindows()
