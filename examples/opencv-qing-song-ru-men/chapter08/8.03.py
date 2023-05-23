# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread('erode.bmp')
kernel = np.ones((9, 9), np.uint8)
img_erode = cv.erode(img, kernel, iterations=5)
cv.imshow('img', img)
cv.imshow('erode', img_erode)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://bit.ly/40vokNv
