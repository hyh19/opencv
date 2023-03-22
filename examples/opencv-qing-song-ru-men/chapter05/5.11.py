# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread("lena.bmp")
rows, cols = img.shape[:2]
map_row = np.zeros(img.shape[:2], np.float32)
map_col = np.zeros(img.shape[:2], np.float32)
for r in range(rows):
    for c in range(cols):
        map_row.itemset((r, c), r)
        map_col.itemset((r, c), c)
rst = cv.remap(img, map_col, map_row, cv.INTER_LINEAR)
cv.imshow("original", img)
cv.imshow("result", rst)
cv.waitKey()
cv.destroyAllWindows()
