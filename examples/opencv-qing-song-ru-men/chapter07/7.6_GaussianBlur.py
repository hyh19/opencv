# -*- coding: utf-8 -*-
import cv2 as cv

o = cv.imread("image/lenaNoise.png")
r = cv.GaussianBlur(o, (5, 5), 0, 0)
cv.imshow("original", o)
cv.imshow("result", r)
cv.waitKey()
cv.destroyAllWindows()
