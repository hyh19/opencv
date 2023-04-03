# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://is.gd/6g4QEI

img = cv.imread("lena.bmp", cv.IMREAD_COLOR)
mask = np.zeros(img.shape, dtype=np.uint8)
mask[100:400, 200:400] = 255
mask[100:500, 100:200] = 255
result = cv.bitwise_and(img, mask)
cv.imshow("img", img)
cv.imshow("mask", mask)
cv.imshow("result", result)
cv.waitKey()
cv.destroyAllWindows()
