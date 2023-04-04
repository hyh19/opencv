# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread('lena.bmp')
rows, cols = img.shape[:2]
map_row = np.zeros(img.shape[:2], np.float32)
map_col = np.zeros(img.shape[:2], np.float32)
for r in range(rows):
    for c in range(cols):
        if 0.25 * rows < r < 0.75 * rows and 0.25 * cols < c < 0.75 * cols:
            # 先缩放，后平移
            map_row.itemset((r, c), 2 * r - rows * 0.5 + 0.5)
            map_col.itemset((r, c), 2 * c - cols * 0.5 + 0.5)
        else:
            map_row.itemset((r, c), 0)
            map_col.itemset((r, c), 0)
rst = cv.remap(img, map_col, map_row, cv.INTER_LINEAR)
cv.imshow('original', img)
cv.imshow('result', rst)
cv.waitKey()
cv.destroyAllWindows()
