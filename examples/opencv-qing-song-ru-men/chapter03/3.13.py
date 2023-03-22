# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

lena = cv.imread("lena.bmp", cv.IMREAD_GRAYSCALE)
cv.imshow("lena", lena)
r, c = lena.shape
x = np.zeros((r, c, 8), dtype=np.uint8)
for i in range(8):
    x[:, :, i] = 2 ** i
planes = np.zeros((r, c, 8), dtype=np.uint8)
for i in range(8):
    planes[:, :, i] = cv.bitwise_and(lena, x[:, :, i])
    mask = planes[:, :, i] > 0
    planes[mask] = 255
    cv.imshow(str(i), planes[:, :, i])
cv.waitKey()
cv.destroyAllWindows()
