# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://bit.ly/3T3oh8z

img = cv.imread("lena.bmp")
height, width = img.shape[:2]
x = 100
y = 200
M = np.float32([[1, 0, x], [0, 1, y]])
move = cv.warpAffine(img, M, (width, height))
cv.imshow("original", img)
cv.imshow("move", move)
cv.waitKey()
cv.destroyAllWindows()
