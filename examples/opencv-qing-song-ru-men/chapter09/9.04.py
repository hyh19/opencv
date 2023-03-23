# -*- coding: utf-8 -*-
import cv2 as cv

img_gray = cv.imread('sobel4.bmp', cv.IMREAD_GRAYSCALE)
sobel_y = cv.Sobel(img_gray, cv.CV_64F, 0, 1)
sobel_y = cv.convertScaleAbs(sobel_y)
cv.imshow("img_gray", img_gray)
cv.imshow("sobel_y", sobel_y)
cv.waitKey()
cv.destroyAllWindows()
