# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread("image/lenaNoise.png")
r = cv.medianBlur(o, 3)
cv.imshow("original", o)
cv.imshow("result", r)
cv.waitKey()
cv.destroyAllWindows()
