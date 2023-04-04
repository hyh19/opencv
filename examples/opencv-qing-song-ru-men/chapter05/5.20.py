# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# 运行结果 https://is.gd/AbUwVz

img = cv.imread('lena.bmp')
row_size, col_size = img.shape[:2]
map_row = np.zeros(img.shape[:2], np.float32)
map_col = np.zeros(img.shape[:2], np.float32)

for row in range(row_size):
    for col in range(col_size):
        if (0.25 * row_size < row < 0.75 * row_size) and (0.25 * col_size < col < 0.75 * col_size):
            # 先缩放，后平移
            map_row.itemset((row, col), 2 * row - row_size * 0.5 + 0.5)
            map_col.itemset((row, col), 2 * col - col_size * 0.5 + 0.5)
        else:
            map_row.itemset((row, col), 0)
            map_col.itemset((row, col), 0)

res = cv.remap(img, map_col, map_row, cv.INTER_LINEAR)
cv.imshow('img', img)
cv.imshow('res', res)
cv.waitKey()
cv.destroyAllWindows()
