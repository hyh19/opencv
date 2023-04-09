# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread('erode.bmp')
kernel = np.ones((5, 5), np.uint8)
erode_img = cv.erode(img, kernel)
cv.imshow('img', img)
cv.imshow('erode', erode_img)
cv.waitKey()
cv.destroyAllWindows()
