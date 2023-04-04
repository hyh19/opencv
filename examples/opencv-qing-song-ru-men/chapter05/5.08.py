# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://is.gd/wAIaTP

img = cv.imread('demo.bmp')
ySize, xSize = img.shape[:2]

p1 = [150, 50]
p2 = [400, 50]
p3 = [60, 450]
p4 = [310, 450]
pts1 = np.float32([p1, p2, p3, p4])

q1 = [50, 50]
q2 = [ySize - 50, 50]
q3 = [50, xSize - 50]
q4 = [ySize - 50, xSize - 50]
pts2 = np.float32([q1, q2, q3, q4])

M = cv.getPerspectiveTransform(pts1, pts2)
res = cv.warpPerspective(img, M, (xSize, ySize))

cv.imshow('img', img)
cv.imshow('res', res)
cv.waitKey()
cv.destroyAllWindows()
