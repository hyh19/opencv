# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread('lena.bmp')
row_size, col_size = img.shape[:2]
row_map = np.zeros(img.shape[:2], np.float32)
col_map = np.zeros(img.shape[:2], np.float32)

for row in range(row_size):
    for col in range(col_size):
        if (0.25 * row_size < row < 0.75 * row_size) and (0.25 * col_size < col < 0.75 * col_size):
            # 先缩放，后平移
            row_map.itemset((row, col), 2 * row - row_size * 0.5 + 0.5)
            col_map.itemset((row, col), 2 * col - col_size * 0.5 + 0.5)
        else:
            row_map.itemset((row, col), 0)
            col_map.itemset((row, col), 0)

res = cv.remap(img, col_map, row_map, cv.INTER_LINEAR)
cv.imshow('img', img)
cv.imshow('res', res)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/AbUwVz
