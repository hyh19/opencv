# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://bit.ly/3Jnr5ZV

img = cv.imread('lena.bmp')
rows, cols, ch = img.shape
p1 = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1]])
p2 = np.float32([[0, rows * 0.33], [cols * 0.85, rows * 0.25], [cols * 0.15, rows * 0.7]])
M = cv.getAffineTransform(p1, p2)
dst = cv.warpAffine(img, M, (cols, rows))
cv.imshow("origianl", img)
cv.imshow("result", dst)
cv.waitKey()
cv.destroyAllWindows()
