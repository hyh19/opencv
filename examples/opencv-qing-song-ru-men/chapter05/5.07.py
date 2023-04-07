# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

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

pts1 = pts1.astype(np.int32)
pts2 = pts2.astype(np.int32)
for p, q in zip(pts1, pts2):
    cv.circle(img, p, 10, (0, 0, 255), -1)
    cv.circle(res, q, 10, (255, 0, 0), -1)

cv.imshow('img', img)
cv.imshow('res', res)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/tw2t0F
