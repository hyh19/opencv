# -*- coding: utf-8 -*-
import cv2 as cv

img_gray = cv.imread("lena.bmp", cv.IMREAD_GRAYSCALE)
img1_canny = cv.Canny(img_gray, 128, 200)
img2_canny = cv.Canny(img_gray, 32, 128)
cv.imshow("gray", img_gray)
cv.imshow("canny1", img1_canny)
cv.imshow("canny2", img2_canny)
cv.waitKey()
cv.destroyAllWindows()

# 运行结果 https://is.gd/M8Br0O
