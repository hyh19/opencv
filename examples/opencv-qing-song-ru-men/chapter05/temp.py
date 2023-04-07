import cv2 as cv
import numpy as np

img = np.random.randint(0, 256, size=(4, 5), dtype=np.uint8)
row_size, col_size = img.shape
row_map = np.zeros(img.shape, np.float32)
col_map = np.zeros(img.shape, np.float32)

for row in range(row_size):
    for col in range(col_size):
        row_map.itemset((row, col), row)
        col_map.itemset((row, col), col)

res = cv.remap(img, col_map, row_map, cv.INTER_LINEAR)
print(f'img = \n{img}')
print(f'row_map = \n{row_map}')
print(f'col_map = \n{col_map}')
print(f'res = \n{res}')
