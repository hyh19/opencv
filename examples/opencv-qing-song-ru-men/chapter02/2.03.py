# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# -----------蓝色通道值--------------
blue = np.zeros((300, 300, 3), dtype=np.uint8)
blue[:, :, 0] = 255
print("blue=\n", blue)
cv.imshow("blue", blue)

# -----------绿色通道值--------------
green = np.zeros((300, 300, 3), dtype=np.uint8)
green[:, :, 1] = 255
print("green=\n", green)
cv.imshow("green", green)

# -----------红色通道值--------------
red = np.zeros((300, 300, 3), dtype=np.uint8)
red[:, :, 2] = 255
print("red=\n", red)
cv.imshow("red", red)

# -----------释放窗口--------------
cv.waitKey()
cv.destroyAllWindows()
