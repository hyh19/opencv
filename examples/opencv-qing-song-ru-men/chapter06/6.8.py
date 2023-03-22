# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread("lena.bmp")
t, rst = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)
cv.imshow("img", img)
cv.imshow("rst", rst)
cv.waitKey()
cv.destroyAllWindows()
