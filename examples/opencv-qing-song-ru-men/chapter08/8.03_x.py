# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://bit.ly/40vokNv

img = cv.imread('erode.bmp', cv.IMREAD_UNCHANGED)
kernel = np.ones((9, 9), np.uint8)
erode = cv.erode(img, kernel, iterations=5)
cv.imshow('img', img)
cv.imshow('erode', erode)
cv.waitKey()
cv.destroyAllWindows()