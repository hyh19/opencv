# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread("lena.bmp", 0)
cv.imshow("before", img)
for i in range(10, 100):
    for j in range(80, 100):
        img[i, j] = 255
cv.imshow("after", img)
cv.waitKey()
cv.destroyAllWindows()
