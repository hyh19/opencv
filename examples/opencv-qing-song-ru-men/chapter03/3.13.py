# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://is.gd/a1Xfr6

gray = cv.imread("lena.bmp", cv.IMREAD_GRAYSCALE)
cv.imshow("gray", gray)

rows, cols = gray.shape
planes = np.zeros((rows, cols, 8), dtype=np.uint8)
for i in range(8):
    bit_plane = cv.bitwise_and(gray, (2 ** i) * np.ones((rows, cols), dtype=np.uint8))
    bit_plane[bit_plane > 0] = 255
    cv.imshow(f'bit plane {i}', bit_plane)
    planes[:, :, i] = bit_plane

cv.waitKey()
cv.destroyAllWindows()
