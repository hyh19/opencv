# -*- coding: utf-8 -*-
import cv2 as cv

gray_img = cv.imread("lena.bmp", cv.IMREAD_GRAYSCALE)
canny_img1 = cv.Canny(gray_img, 128, 200)
canny_img2 = cv.Canny(gray_img, 32, 128)
cv.imshow("gray", gray_img)
cv.imshow("canny1", canny_img1)
cv.imshow("canny2", canny_img2)
cv.waitKey()
cv.destroyAllWindows()
