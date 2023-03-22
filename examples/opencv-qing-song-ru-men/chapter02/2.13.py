# -*- coding: utf-8 -*-
import cv2 as cv

a = cv.imread("lenacolor.png", cv.IMREAD_UNCHANGED)
face = a[220:400, 250:350]
cv.imshow("original", a)
cv.imshow("face", face)
cv.waitKey()
cv.destroyAllWindows()
