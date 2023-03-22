# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=[4, 5], dtype=np.uint8)
rows, cols = img.shape
map_row = np.zeros(img.shape, np.float32)
map_col = np.zeros(img.shape, np.float32)
for r in range(rows):
    for c in range(cols):
        map_row.itemset((r, c), r)
        map_col.itemset((r, c), c)
rst = cv.remap(img, map_col, map_row, cv.INTER_LINEAR)
print("img=\n", img)
print("map_row=\n", map_row)
print("map_col=\n", map_col)
print("rst=\n", rst)
