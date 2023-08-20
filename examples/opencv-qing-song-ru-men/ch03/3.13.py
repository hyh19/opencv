# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

gray = cv.imread('lena.bmp', cv.IMREAD_GRAYSCALE)
cv.imshow('gray', gray)

rows, cols = gray.shape
for i in range(8):
    extract = np.ones(gray.shape, dtype=np.uint8) * (2 ** i)
    bit_plane = cv.bitwise_and(gray, extract)
    bit_plane[bit_plane > 0] = 255
    cv.imshow(f'bit plane {i}', bit_plane)

cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/a1Xfr6
