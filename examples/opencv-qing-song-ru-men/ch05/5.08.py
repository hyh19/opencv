# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread('demo.bmp')
rows, cols = img.shape[:2]
width, height = cols, rows

p1 = (150, 50)
p2 = (400, 50)
p3 = (60, 450)
p4 = (310, 450)
pts1 = np.float32([p1, p2, p3, p4])

q1 = (50, 50)
q2 = (height - 50, 50)
q3 = (50, width - 50)
q4 = (height - 50, width - 50)
pts2 = np.float32([q1, q2, q3, q4])

M = cv.getPerspectiveTransform(pts1, pts2)
res = cv.warpPerspective(img, M, (width, height))

pts1 = pts1.astype(np.int32)
pts2 = pts2.astype(np.int32)
for p, q in zip(pts1, pts2):
    cv.circle(img, p, 5, (0, 0, 255), -1)
    cv.circle(res, q, 5, (255, 0, 0), -1)

cv.imshow('img', img)
cv.imshow('res', res)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/xyoKtL
