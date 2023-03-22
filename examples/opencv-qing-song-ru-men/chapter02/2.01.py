# -*- coding: utf-8 -*-
import cv2 as cv as cv
import numpy as np

img = np.zeros((8, 8), dtype=np.uint8)
print("img=\n", img)
print("读取像素点img[0,3]=", img[0, 3])
cv.imshow("one", img)

img[0, 3] = 255
print("修改后img=\n", img)
print("读取修改后像素点img[0,3]=", img[0, 3])
cv.imshow("two", img)

cv.waitKey()
cv.destroyAllWindows()
