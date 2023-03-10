# -*- coding: utf-8 -*-
import cv2
import numpy as np

lena = cv2.imread("lena.bmp", cv2.IMREAD_GRAYSCALE)
cv2.imshow("lena", lena)
r, c = lena.shape
x = np.zeros((r, c, 8), dtype=np.uint8)
for i in range(8):
    x[:, :, i] = 2 ** i
planes = np.zeros((r, c, 8), dtype=np.uint8)
for i in range(8):
    planes[:, :, i] = cv2.bitwise_and(lena, x[:, :, i])
    mask = planes[:, :, i] > 0
    planes[mask] = 255
    cv2.imshow(str(i), planes[:, :, i])
cv2.waitKey()
cv2.destroyAllWindows()
