# -*- coding: utf-8 -*-
import cv2 as cv

lena = cv.imread("lenacolor.png")
rgb = cv.cvtColor(lena, cv.COLOR_BGR2RGB)
bgr = cv.cvtColor(rgb, cv.COLOR_RGB2BGR)
cv.imshow("lena", lena)
cv.imshow("rgb", rgb)
cv.imshow("bgr", bgr)
cv.waitKey()
cv.destroyAllWindows()
