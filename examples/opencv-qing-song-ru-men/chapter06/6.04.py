# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://is.gd/8bZ6d7

img = cv.imread("lena.bmp")
thresh, res = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
cv.imshow("img", img)
cv.imshow("res", res)
cv.waitKey()
cv.destroyAllWindows()
