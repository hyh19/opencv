# -*- coding: utf-8 -*-
import cv2 as cv

lena = cv.imread("lenacolor.png")
cv.imshow("lena1", lena)
b = lena[:, :, 0]
g = lena[:, :, 1]
r = lena[:, :, 2]
cv.imshow("b", b)
cv.imshow("g", g)
cv.imshow("r", r)
lena[:, :, 0] = 0
cv.imshow("lenab0", lena)
lena[:, :, 1] = 0
cv.imshow("lenab0g0", lena)
cv.waitKey()
cv.destroyAllWindows()
