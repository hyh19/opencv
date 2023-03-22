# -*- coding: utf-8 -*-
import cv2 as cv

lena = cv.imread("lenacolor.png")
b, g, r = cv.split(lena)
bgr = cv.merge([b, g, r])
rgb = cv.merge([r, g, b])
cv.imshow("lena", lena)
cv.imshow("bgr", bgr)
cv.imshow("rgb", rgb)
cv.waitKey()
cv.destroyAllWindows()
