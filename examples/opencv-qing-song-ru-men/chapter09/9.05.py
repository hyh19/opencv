# -*- coding: utf-8 -*-
import cv2 as cv

img_gray = cv.imread("sobel4.bmp", cv.IMREAD_GRAYSCALE)
sobel_xy = cv.Sobel(img_gray, cv.CV_64F, 1, 1)
sobel_xy = cv.convertScaleAbs(sobel_xy)
cv.imshow("img_gray", img_gray)
cv.imshow("sobel_xy", sobel_xy)
cv.waitKey()
cv.destroyAllWindows()
