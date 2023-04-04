# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://is.gd/kdxQZk

img = cv.imread('lena.bmp')
ySize, xSize = img.shape[:2]

p1 = [0, 0]
p2 = [xSize - 1, 0]
p3 = [0, ySize - 1]
pts1 = np.float32([p1, p2, p3])

q1 = [0, ySize * 0.33]
q2 = [xSize * 0.85, ySize * 0.25]
q3 = [xSize * 0.15, ySize * 0.7]
pts2 = np.float32([q1, q2, q3])

M = cv.getAffineTransform(pts1, pts2)
res = cv.warpAffine(img, M, (xSize, ySize))

cv.imshow('img', img)
cv.imshow('res', res)
cv.waitKey()
cv.destroyAllWindows()
