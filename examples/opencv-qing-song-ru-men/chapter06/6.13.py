# -*- coding: utf-8 -*-
import cv2 as cv

img = cv.imread("tiffany.bmp", 0)
t1, thd = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
t2, otsu = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
cv.imshow("img", img)
cv.imshow("thd", thd)
cv.imshow("otus", otsu)
cv.waitKey()
cv.destroyAllWindows()
