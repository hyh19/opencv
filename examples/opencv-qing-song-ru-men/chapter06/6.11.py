# -*- coding: utf-8 -*-
import cv2 as cv

# 运行结果 https://is.gd/mtQHx6

img = cv.imread("computer.jpg", cv.IMREAD_GRAYSCALE)
thresh, res = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
mean = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, 5)
gaussian = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 3, 5)

cv.imshow("img", img)
cv.imshow("res", res)
cv.imshow("mean", mean)
cv.imshow("gaussian", gaussian)

cv.waitKey()
cv.destroyAllWindows()
