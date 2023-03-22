# -*- coding: utf-8 -*-
import cv2 as cv

lena = cv.imread("lenacolor.png")
gray = cv.cvtColor(lena, cv.COLOR_BGR2GRAY)
rgb = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
# ==========打印shape============
print("lena.shape=", lena.shape)
print("gray.shape=", gray.shape)
print("rgb.shape=", rgb.shape)
# ==========显示效果============
cv.imshow("lena", lena)
cv.imshow("gray", gray)
cv.imshow("rgb", rgb)
cv.waitKey()
cv.destroyAllWindows()
