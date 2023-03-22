# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread("image/lenaNoise.png")
r = cv.boxFilter(o, -1, (5, 5))
cv.imshow("original", o)
cv.imshow("result", r)
cv.waitKey()
cv.destroyAllWindows()
