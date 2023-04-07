import cv2 as cv
import numpy as np

img = cv.imread('lena.bmp')
row_size, col_size = img.shape[:2]
row_map = np.zeros(img.shape[:2], np.float32)
col_map = np.zeros(img.shape[:2], np.float32)

for row in range(row_size):
    for col in range(col_size):
        row_map.itemset((row, col), row_size - 1 - row)
        col_map.itemset((row, col), col)

res = cv.remap(img, col_map, row_map, cv.INTER_LINEAR)
cv.imshow('img', img)
cv.imshow('res', res)
cv.waitKey()
cv.destroyAllWindows()
