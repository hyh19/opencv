# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread('erode.bmp')
kernel = np.ones(shape=(5, 5), dtype=np.uint8)
img_erode = cv.erode(img, kernel)
cv.imshow('img', img)
cv.imshow('erode', img_erode)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/k8JZrI
