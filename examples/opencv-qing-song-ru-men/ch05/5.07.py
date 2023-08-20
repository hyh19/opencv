# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread('lena.bmp')
rows, cols = img.shape[:2]
width, height = cols, rows

p1 = (0, 0)
p2 = (width - 1, 0)
p3 = (0, height - 1)
pts1 = np.float32([p1, p2, p3])

q1 = (0, height * 0.33)
q2 = (width * 0.85, height * 0.25)
q3 = (width * 0.15, height * 0.7)
pts2 = np.float32([q1, q2, q3])

M = cv.getAffineTransform(pts1, pts2)
res = cv.warpAffine(img, M, (width, height))

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
