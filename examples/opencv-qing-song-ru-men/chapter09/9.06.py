# -*- coding: utf-8 -*-
import cv2 as cv

img_gray = cv.imread("sobel4.bmp", cv.IMREAD_GRAYSCALE)

sobel_x = cv.Sobel(img_gray, cv.CV_64F, 1, 0)
sobel_x = cv.convertScaleAbs(sobel_x)

sobel_y = cv.Sobel(img_gray, cv.CV_64F, 0, 1)
sobel_y = cv.convertScaleAbs(sobel_y)

sobel_xy = cv.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

cv.imshow("img_gray", img_gray)
cv.imshow("sobel_x", sobel_x)
cv.imshow("sobel_y", sobel_y)
cv.imshow("sobel_xy", sobel_xy)

cv.waitKey()
cv.destroyAllWindows()
