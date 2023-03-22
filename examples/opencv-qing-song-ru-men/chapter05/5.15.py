# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = cv2.imread("lena.bmp")
rows, cols = img.shape[:2]
map_row = np.zeros(img.shape[:2], np.float32)
map_col = np.zeros(img.shape[:2], np.float32)
for r in range(rows):
    for c in range(cols):
        map_row.itemset((r, c), r)
        map_col.itemset((r, c), cols - 1 - c)
rst = cv2.remap(img, map_col, map_row, cv2.INTER_LINEAR)
cv2.imshow("original", img)
cv2.imshow("result", rst)
cv2.waitKey()
cv2.destroyAllWindows()
