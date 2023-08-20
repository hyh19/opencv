# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread('lena.bmp')
row_size, col_size = img.shape[:2]
map_row = np.zeros(img.shape[:2], np.float32)
map_col = np.zeros(img.shape[:2], np.float32)

for row in range(row_size):
    for col in range(col_size):
        map_row.itemset((row, col), row_size - 1 - row)
        map_col.itemset((row, col), col_size - 1 - col)

res = cv.remap(img, map_col, map_row, cv.INTER_LINEAR)
cv.imshow('img', img)
cv.imshow('res', res)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/lbrwGp
