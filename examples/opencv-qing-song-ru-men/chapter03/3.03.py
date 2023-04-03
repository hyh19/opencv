# -*- coding: utf-8 -*-
import cv2 as cv

img_gray = cv.imread("lena.bmp", cv.IMREAD_GRAYSCALE)
img_copy = img_gray.copy()
result1 = img_gray + img_copy
result2 = cv.add(img_gray, img_copy)
cv.imshow("Original", img_gray)
cv.imshow("Result1", result1)
cv.imshow("Result2", result2)
cv.waitKey()
cv.destroyAllWindows()
