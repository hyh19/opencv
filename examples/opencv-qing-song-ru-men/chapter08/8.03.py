# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread('erode.bmp', cv.IMREAD_UNCHANGED)
kernel = np.ones((9, 9), np.uint8)
erode_img = cv.erode(img, kernel, iterations=5)
cv.imshow('img', img)
cv.imshow('erode', erode_img)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://bit.ly/40vokNv
