# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://bit.ly/3J5rOOT

img = cv.imread('demo.bmp')
rows, cols = img.shape[:2]
print(rows, cols)
pts1 = np.float32([[150, 50], [400, 50], [60, 450], [310, 450]])
pts2 = np.float32([[50, 50], [rows - 50, 50], [50, cols - 50], [rows - 50, cols - 50]])
M = cv.getPerspectiveTransform(pts1, pts2)
dst = cv.warpPerspective(img, M, (cols, rows))
cv.imshow("img", img)
cv.imshow("dst", dst)
cv.waitKey()
cv.destroyAllWindows()
